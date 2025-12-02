import { useState, useRef, useEffect } from 'react';
import './llmInterface.css';

function LLMInterface() {
    const [messages, setMessages] = useState([
        { id: 1, text: "Hello. How can I assist you today?", sender: 'bot' }
    ]);
    const [inputValue, setInputValue] = useState('');
    const [isLoading, setIsLoading] = useState(false);
    const messagesEndRef = useRef(null);
    const textareaRef = useRef(null);

    const scrollToBottom = () => {
        messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
    };

    useEffect(() => {
        scrollToBottom();
    }, [messages, isLoading]);

    // Auto-resize textarea
    useEffect(() => {
        if (textareaRef.current) {
            textareaRef.current.style.height = 'auto';
            textareaRef.current.style.height = textareaRef.current.scrollHeight + 'px';
        }
    }, [inputValue]);

    const handleSendMessage = async (e) => {
        e.preventDefault();
        if (!inputValue.trim()) return;

        const userMessage = {
            id: Date.now(),
            text: inputValue,
            sender: 'user'
        };

        setMessages(prev => [...prev, userMessage]);
        setInputValue('');
        setIsLoading(true);

        // Reset height
        if (textareaRef.current) {
            textareaRef.current.style.height = 'auto';
        }

        // Mock streaming response
        setTimeout(() => {
            setIsLoading(false);
            const botMessage = {
                id: Date.now() + 1,
                text: "I am a helpful AI assistant. I can help you with coding, writing, and analysis.",
                sender: 'bot'
            };
            setMessages(prev => [...prev, botMessage]);
        }, 1500);
    };

    const handleKeyDown = (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            handleSendMessage(e);
        }
    };

    return (
        <div className="app-container">
            {/* Main Chat Area */}
            <main className="chat-interface">
                <header className="chat-header">
                    <div className="model-name">KTH-GPT</div>
                </header>

                <div className="messages-container">
                    {messages.map((msg) => (
                        <div key={msg.id} className={`message-row ${msg.sender}`}>
                            <div className="message-content">
                                {msg.sender === 'bot' && <div className="bot-icon">AI</div>}
                                <div className="bubble">
                                    {msg.text}
                                </div>
                            </div>
                        </div>
                    ))}
                    {isLoading && (
                        <div className="message-row bot">
                            <div className="message-content">
                                <div className="bot-icon">AI</div>
                                <div className="bubble loading">
                                    <span className="dot"></span>
                                    <span className="dot"></span>
                                    <span className="dot"></span>
                                </div>
                            </div>
                        </div>
                    )}
                    <div ref={messagesEndRef} className="spacer" />
                </div>

                <div className="input-area-wrapper">
                    <div className="input-box">
                        <textarea
                            ref={textareaRef}
                            value={inputValue}
                            onChange={(e) => setInputValue(e.target.value)}
                            onKeyDown={handleKeyDown}
                            placeholder="Message..."
                            rows={1}
                        />
                        <button
                            className="send-btn"
                            disabled={!inputValue.trim() || isLoading}
                            onClick={handleSendMessage}
                        >
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                                <line x1="22" y1="2" x2="11" y2="13"></line>
                                <polygon points="22 2 15 22 11 13 2 9 22 2"></polygon>
                            </svg>
                        </button>
                    </div>
                    <div className="disclaimer">
                        AI can make mistakes. Please check important information.
                    </div>
                </div>
            </main>
        </div>
    );
}

export default LLMInterface;