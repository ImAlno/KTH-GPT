from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
import os
import pandas as pd

# Load CSV
df = pd.read_csv("realistic_restaurant_reviews.csv")
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

# Path to FAISS index
db_location = "faiss_index"
add_documents = not os.path.exists(db_location)

if add_documents:
    documents = []
    ids = []

    for i, row in df.iterrows():
        document = Document(
            page_content=row["Title"] + " " + row["Review"],
            metadata={"rating": row["Rating"], "date": row["Date"]},
            id=str(i)
        )
        documents.append(document)
        ids.append(str(i))

    # Build FAISS index from documents
    vector_store = FAISS.from_documents(documents, embedding=embeddings)
    vector_store.save_local(db_location)

else:
    # Load existing FAISS index
    vector_store = FAISS.load_local(
        db_location,
        embeddings,
        allow_dangerous_deserialization=True
    )

# **This must be at the bottom**
retriever = vector_store.as_retriever(search_kwargs={"k": 5})
