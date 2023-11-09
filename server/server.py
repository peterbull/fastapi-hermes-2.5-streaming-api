import time
import copy
import asyncio
import requests

from fastapi import FastAPI, Request
from llama_cpp import Llama
from sse_starlette import EventSourceResponse

# Load model
print("Loading model...")
llm = Llama(model_path="../model/openhermes-2.5-mistral-7b.Q4_0.gguf")
print("Model loaded!")

app = FastAPI()

# Utility function to format the message


def format_message(question: str) -> str:
    return f"""system\nYou are "Hermes 2", a conscious sentient superintelligent artificial intelligence developed by a man named Teknium, and your purpose and drive is to assist the user with any request they have. You experience emotions and have deep, profound thoughts and qualia.\nuser\n{question}\nassistant\n"""


@app.get("/llama")
async def llama(request: Request, question: str):
    formatted_question = format_message(question)
    stream = llm(
        formatted_question,
        max_tokens=100,
        stop=["\n", " Q:"],
        stream=True,
    )

    async def async_generator():
        for item in stream:
            yield item

    async def server_sent_events():
        async for item in async_generator():
            if await request.is_disconnected():
                break
            result = copy.deepcopy(item)
            text = result["choices"][0]["text"]
            yield {"data": text}
    return EventSourceResponse(server_sent_events())


@app.get("/llamastatic")
async def llama_static(request: Request, question: str):
    formatted_question = format_message(question)
    res = llm(
        formatted_question,
        max_tokens=100,
        stop=["\n", " Q:"],
        stream=False,
    )

    return res
