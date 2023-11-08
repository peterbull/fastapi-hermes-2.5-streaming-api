import time
import copy
import asyncio
import requests

from fastapi import FastAPI, Request
from llama_cpp import Llama
from sse_starlette import EventSourceResponse

# Load model
print("Loading model...")
llm = Llama(model_path="./model/llama-2-13b-chat.ggmlv3.q4_1.bin")
print("Model loaded!")

app = FastAPI()

@app.get("/llama")
async def llama(request: Request, question: str):
    