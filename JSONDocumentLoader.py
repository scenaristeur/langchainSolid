from langchain.docstore.document import Document
from langchain.document_loaders.base import BaseLoader
from pyld import jsonld
import json

# utile ? asynch loader
jsonld.set_document_loader(jsonld.aiohttp_document_loader(timeout=1000))

import hashlib
from datetime import datetime



class JSONDocumentLoader(BaseLoader):
    def __init__(self, url: str):
        self.url = url
        print("scanning", self.url)
        


    def load(self) -> list[Document]:
        flattened = jsonld.flatten(self.url)
       # print(json.dumps(flattened, indent=2))

   

        for i in flattened:
            print("--", i['@id'])
        documents = self.parse(flattened)

        return documents
# see https://github.com/hwchase17/langchain/blob/master/langchain/document_loaders/json_loader.py
    def parse(self, json_data) -> list[Document]:
        documents = []

        hash = hashlib.md5(json.dumps(json_data).encode())
        print("The hexadecimal equivalent of hash is : ", end ="")
        print(hash.hexdigest())


        for item in json_data:
           # print(json.dumps(item, indent=2))
            document = Document(
                metadata={
                    # Set the metadata properties based on the JSON data
                    # Example:
                    "source": self.url,
                    "hash": hash.hexdigest(),
                    "date":  datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
                    # ...
                },
                # Set the page content based on the JSON data
                page_content=json.dumps(item),
            )
            documents.append(document)
            if '@type' in item :
                print("type", item['@type'])
                if 'http://www.w3.org/ns/ldp#BasicContainer' in item['@type'] or 'http://www.w3.org/ns/ldp#Container' in item['@type']: 
                    
                    JSONDocumentLoader(item['@id'])
            else:
                print("no type")

        return documents


#loader = JSONDocumentLoader("https://spoggy-test4.solidcommunity.net/public/"
   #                         , {
    # "Authorization": "Bearer <token>",
    #'Accept': 'application/ld+json',
#}
#)
                            
#loader = JSONDocumentLoader("https://spoggy-test4.solidcommunity.net/profile/card#me")
"""loader = JSONDocumentLoader("https://spoggy-test4.solidcommunity.net/public/")

documents = loader.load()


print("\n",len(documents), "loaded")
document = documents[-1]
print(document.page_content[0:50])

pdf_metadata = document.metadata
print (pdf_metadata) """



#print("\n######################\nMULTI\n######################\n")
# https://learn.deeplearning.ai/langchain-chat-with-your-data/lesson/4/vectorstores-and-embedding

# Load PDF
loaders = [
    # Duplicate documents on purpose - messy data
    JSONDocumentLoader("https://spoggy-test5.solidcommunity.net/public/"),
  #  JSONDocumentLoader("https://spoggy-test2.solidcommunity.net/public/"),
  #  JSONDocumentLoader("https://spoggy-test3.solidcommunity.net/public/"),
  #  JSONDocumentLoader("https://spoggy-test4.solidcommunity.net/profile/card#me"),
   # JSONDocumentLoader("https://spoggy-test5.solidcommunity.net/profile/card#me"),
   # JSONDocumentLoader("https://spoggy-test3.solidcommunity.net/profile/card#me"),
    #JSONDocumentLoader("https://spoggy-test2.solidcommunity.net/profile/card#me"),
]
docs = []
for loader in loaders:
    docs.extend(loader.load())
    print("\n",len(docs), "loaded")

print("\n",len(docs), "loaded")

# Split
from langchain.text_splitter import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1500,
    chunk_overlap = 150
)
splits = text_splitter.split_documents(docs)
print("Splits",len(splits))


import os
import openai
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key  = os.environ['OPENAI_API_KEY']

from langchain.embeddings.openai import OpenAIEmbeddings
embedding = OpenAIEmbeddings()


"""
sentence1 = "i like dogs"
sentence2 = "i like canines"
sentence3 = "the weather is ugly outside"

embedding1 = embedding.embed_query(sentence1)
embedding2 = embedding.embed_query(sentence2)
embedding3 = embedding.embed_query(sentence3)
import numpy as np
print(np.dot(embedding1, embedding2))
print(np.dot(embedding1, embedding3))
print(np.dot(embedding2, embedding3)) 
"""


#for doc in docs:
 #   print(doc)
    #d = doc[0] # https://github.com/hwchase17/langchain/issues/2222
  #  doc_embedding = embedding.embed_query(doc.to_dict())

from langchain.vectorstores import Chroma
persist_directory = 'docs/chroma/'
# !rm -rf ./docs/chroma  # remove old database files if any
vectordb = Chroma.from_documents(
    documents=docs,
    embedding=embedding,
    persist_directory=persist_directory
)


print(vectordb._collection.count())

question = "what is agora ?"

docs_result = vectordb.similarity_search(question,k=3)
print(len(docs_result))

print("##0",docs_result[0].page_content)
print("##1",docs_result[1].page_content)
print("##2",docs_result[2].page_content)

vectordb.persist()