import os
from dotenv import find_dotenv, load_dotenv
from langchain.llms import OpenAI


load_dotenv(find_dotenv())
api_key = os.getenv("OPENAI_API_KEY")

llm = OpenAI(
        openai_api_key=api_key
)

result = llm("Write a very very short poem")
print(result)

