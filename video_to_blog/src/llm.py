from dotenv import load_dotenv
import os
from langchain.chat_models import init_chat_model

load_dotenv()

llm=init_chat_model("llama-3.1-8b-instant", model_provider="groq")

def llm_call(prompt:str)->str:
    response=llm.invoke(prompt)
    return response.content

