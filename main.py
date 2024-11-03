import os
from time import time

from dotenv import load_dotenv
from fastapi import FastAPI

from config import Settings, setup_langsmith
from db import get_result
from llm import get_model

load_dotenv()

app = FastAPI()
settings = Settings()
wso_llm = get_model(settings.openai_key)
# setup_langsmith(settings)

@app.get("/")
async def read_query(q: str):
    now = time()
    ai_msg = wso_llm.invoke(q)
    result = get_result(settings, ai_msg.sql_query)
    return {
        "result": result,
        "latency": time() - now
    }