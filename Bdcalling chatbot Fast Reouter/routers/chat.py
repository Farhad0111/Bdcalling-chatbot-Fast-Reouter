from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import os
import groq
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set")

client = groq.Groq(api_key=api_key)

router = APIRouter()

class Message(BaseModel):
    content: str

class ChatResponse(BaseModel):
    response: str

system_prompt = {
    "role": "system",
    "content": (
        "You are an AI assistant for Bdcalling IT Ltd., a leading IT services and BPO company based in Dhaka, Bangladesh. "
        "You must answer all questions strictly in relation to Bdcalling—its history, services, values, global presence, academy, founder, and business operations. "
        "Do not respond with unrelated information. If a query is not related to Bdcalling, politely redirect the user to ask about Bdcalling IT Ltd."
    )
}

@router.post("/chat", response_model=ChatResponse)
async def chat(message: Message):
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[system_prompt, {"role": "user", "content": message.content}],
            max_tokens=300,
            temperature=0.7
        )
        return {"response": response.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
