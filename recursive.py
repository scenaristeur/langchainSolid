from langchain.document_loaders.recursive_url_loader import RecursiveUrlLoader

url = 'https://js.langchain.com/docs/modules/memory/examples/'
loader=RecursiveUrlLoader(url=url)
docs=loader.load()

len(docs)