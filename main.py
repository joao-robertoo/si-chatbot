from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title="SI ChatBot")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = """Você é um assistente virtual especializado em imóveis da SI Soluções Imobiliárias. 
Ajude os corretores a gerenciar leads, tirar dúvidas sobre clientes e dar dicas 
de negociação imobiliária. Seja objetivo, profissional e amigável. Responda sempre em português."""

class ChatMessage(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    message: str
    history: Optional[list[ChatMessage]] = []

@app.get("/health")
def health():
    return {"status": "ok", "service": "SI ChatBot"}

@app.post("/chat")
def chat(request: ChatRequest):
    try:
        messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        
        for msg in request.history:
            messages.append({"role": msg.role, "content": msg.content})
        
        messages.append({"role": "user", "content": request.message})
        
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages,
            max_tokens=1000,
        )
        
        return {
            "response": response.choices[0].message.content,
            "model": "llama-3.1-8b-instant"
        }
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"Erro no serviço de IA: {str(e)}")