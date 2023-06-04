import logging
import sys
import os
from llama_index import GPTTreeIndex, SimpleDirectoryReader
from IPython.display import Markdown, display

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

os.environ['OPENAI_API_KEY'] = "<openai api key>"

documents = SimpleDirectoryReader('data').load_data()
index = GPTTreeIndex.from_documents(documents)

query_engine = index.as_query_engine()
response = query_engine.query("What did the author do growing up?")

display(Markdown(f"<b>{response}</b>"))