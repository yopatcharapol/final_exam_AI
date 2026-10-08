
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
from pydantic import BaseModel

from database import (
    init_database,
    create_chat,
    get_chats,
    get_chat,
    add_message,
    get_messages,
    update_chat_title
)

from openrouter_client import call_openrouter, call_openrouter4web


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_database()
    yield


app = FastAPI(lifespan=lifespan)


app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)


templates = Jinja2Templates(directory="templates")


class MessageRequest(BaseModel):
    content: str


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.get("/api/chats")
def list_chats():
    return get_chats()


@app.post("/api/chats")
def new_chat():
    chat_id = create_chat()

    return {
        "id": chat_id,
        "title": "New Chat"
    }


@app.get("/api/chats/{chat_id}")
def get_chat_data(chat_id: int):
    chat = get_chat(chat_id)

    if not chat:
        raise HTTPException(
            status_code=404,
            detail="Chat not found"
        )

    messages = get_messages(chat_id)

    return {
        "chat": chat,
        "messages": messages
    }


@app.post("/api/chats/{chat_id}/messages")
def send_message(
    chat_id: int,
    request: MessageRequest
):
    chat = get_chat(chat_id)

    if not chat:
        raise HTTPException(
            status_code=404,
            detail="Chat not found"
        )

    user_message = request.content.strip()

    if not user_message:
        raise HTTPException(
            status_code=400,
            detail="Message cannot be empty"
        )

    # Save user message
    add_message(
        chat_id,
        "user",
        user_message
    )

    # Get complete conversation history
    history = get_messages(chat_id)

    # Convert database messages to OpenRouter format
    openrouter_messages = [
        {
            "role": message["role"],
            "content": message["content"]
        }
        for message in history
    ]

    try:
        # Call OpenRouter with the complete conversation
        assistant_response = call_openrouter4web(
            openrouter_messages
        )

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error)
        )

    # Save assistant response
    add_message(
        chat_id,
        "assistant",
        assistant_response
    )

    # Change title from New Chat using first user message
    if chat["title"] == "New Chat":
        title = user_message[:40]

        if len(user_message) > 40:
            title += "..."

        update_chat_title(
            chat_id,
            title
        )

    return {
        "role": "assistant",
        "content": assistant_response
    }


@app.get("/api/chats/{chat_id}/messages")
def list_messages(chat_id: int):
    chat = get_chat(chat_id)

    if not chat:
        raise HTTPException(
            status_code=404,
            detail="Chat not found"
        )

    return get_messages(chat_id)

