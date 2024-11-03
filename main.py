import os

from dotenv import load_dotenv
from fastapi import FastAPI
from llm import get_model

load_dotenv()

app = FastAPI()
open_api_key = os.getenv('OPENAI_API_KEY')
wso_llm = get_model(open_api_key)

@app.get("/")
async def read_query(q: str):
    ai_msg = wso_llm.invoke("who is the biggest contributer?")
    return {"query": ai_msg.sql_query}