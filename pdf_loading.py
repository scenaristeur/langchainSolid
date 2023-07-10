# https://learn.deeplearning.ai/langchain-chat-with-your-data/lesson/2/document-loading

import os
import openai
import sys
sys.path.append('../..')

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key  = os.environ['OPENAI_API_KEY']

from langchain.document_loaders import PyPDFLoader
loader = PyPDFLoader("docs/cs229_lectures/MachineLearning-Lecture01.pdf")
pages = loader.load()

len(pages)
page = pages[0]
print(page.page_content[0:500])

pdf_metadate = page.metadata
print (pdf_metadate)