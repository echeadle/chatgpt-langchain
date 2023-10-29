import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())
api_key = os.getenv("OPENAI_API_KEY")

print(api_key)
