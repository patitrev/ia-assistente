import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, validator
import openai
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
import logging

# Logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# FastAPI app initialization
app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Load OpenAI API key from environment variable
openai.api_key = ''

# Conversation history storage
conversation_history = {}

# Request model with validation
class QuestionRequest(BaseModel):
    question: str
    index: int
    empresa: str

    @validator("index")
    def index_must_be_non_negative(cls, value):
        if value < 0:
            raise ValueError("Index must be a non-negative integer")
        return value

@app.post("/ask")
async def ask(request: QuestionRequest):
    question = request.question
    index = request.index
    empresa = request.empresa

    if not question:
        raise HTTPException(status_code=400, detail="Question cannot be empty")

    # Retrieve conversation history
    if empresa not in conversation_history:
        conversation_history[empresa] = []
    history = conversation_history[empresa]

    try:
        # Format conversation history
        messages = [{"role": "system", "content": f"Você é um assistente de uma empresa chamada {empresa}."}]
        for q, a in history:
            messages.append({"role": "user", "content": q})
            messages.append({"role": "assistant", "content": a})
        messages.append({"role": "user", "content": question})

        logger.info(f"Received question: {question} (Index: {index}, Company: {empresa})")

        # Call OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        answer = response.choices[0].message['content'].strip()
        logger.info(f"Generated answer: {answer}")

        # Update conversation history
        conversation_history[empresa].append((question, answer))

        return {"answer": answer}

    except openai.error.RateLimitError as e:
        logger.error(f"OpenAI API rate limit exceeded: {e}")
        raise HTTPException(status_code=429, detail="Rate limit exceeded")
    except openai.error.AuthenticationError as e:
        logger.error(f"OpenAI API authentication error: {e}")
        raise HTTPException(status_code=401, detail="Authentication error")
    except Exception as e:
        logger.error(f"Error processing question: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

# Request model for clearing context
class ClearRequest(BaseModel):
    empresa: str

@app.post("/clear")
async def clear(request: ClearRequest):
    empresa = request.empresa

    if empresa in conversation_history:
        conversation_history[empresa] = []
        logger.info(f"Cleared conversation history for company: {empresa}")
        return {"detail": "Conversation history cleared"}
    else:
        raise HTTPException(status_code=404, detail="Company not found")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)