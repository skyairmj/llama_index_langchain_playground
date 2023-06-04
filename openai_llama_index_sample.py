import logging
import sys
import os
from llama_index import GPTTreeIndex, SimpleDirectoryReader

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

os.environ['OPENAI_API_KEY'] = "<openai api key>"

documents = SimpleDirectoryReader('data').load_data()
index = GPTTreeIndex.from_documents(documents)

query_engine = index.as_query_engine()
query_engine.query("What is the name of the professional women's basketball team in New York City?")

# Try using embedding query
query_engine.query("What are the airports in New York City?", retriever_mode="embedding")