from fastapi import FastAPI
from routers import chat, info

app = FastAPI(
    title="Bdcalling Chatbot",
    description="A chatbot that provides information only about Bdcalling IT Ltd.",
    version="1.0.0"
)

app.include_router(chat.router, prefix="/api")
app.include_router(info.router)
