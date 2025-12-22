from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from utils import get_results_rerank

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Model and Prompts
model = OllamaLLM(model="llama3.2")

template = """
1. You are a highly helpful, precise assistant. Provide as much detail as you can in your answers.
2. Answer the user's question using the ONLY the provided context. 
3. If something is unclear you are allowed use the context as a guideline, explain all mentioned concepts in the context.

context:
{results}

User’s question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

class QuestionRequest(BaseModel):
    question: str

class AnswerResponse(BaseModel):
    answer: str

@app.post("/ask", response_model=AnswerResponse)
async def ask_question(request: QuestionRequest):
    try:
        question = request.question
        if not question:
            raise HTTPException(status_code=400, detail="Question cannot be empty")
        
        # Retrieve context with reranking
        results = get_results_rerank(question, 4)
        
        # Invoke chain
        result = chain.invoke({"results": results, "question": question})
        
        return AnswerResponse(answer=result)
    except Exception as e:
        # Log the error if needed
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
