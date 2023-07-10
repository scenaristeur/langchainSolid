#!pip install lark


import os
import openai
import sys
sys.path.append('../..')

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key  = os.environ['OPENAI_API_KEY']

from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
embedding = OpenAIEmbeddings()
persist_directory = 'docs/chroma/'


#embedding = OpenAIEmbeddings()
vectordb = Chroma(
    persist_directory=persist_directory,
    embedding_function=embedding
)


print(vectordb._collection.count())


#question = "What is hospex ?"
question = "who knows https://spoggy-test5.solidcommunity.net/profile/card#me ?"
question = "what are the name of  https://spoggy-test5.solidcommunity.net/profile/card#me 'http://xmlns.com/foaf/0.1/knows' <name> ?"


print("##",question,"##")

#docs_result = vectordb.similarity_search(question,k=3)
# SentenceTransformerEmbeddingFunction
docs_result = vectordb.max_marginal_relevance_search(question,k=3, fetch_k=5)
print(len(docs_result))

print("##0",docs_result[0].page_content)
print("##1",docs_result[1].page_content)
print("##2",docs_result[2].page_content)