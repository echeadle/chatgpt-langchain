from langchain.document_loaders import TextLoader

from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

loader = TextLoader("facts.txt")
docs = loader.load()

print(docs)