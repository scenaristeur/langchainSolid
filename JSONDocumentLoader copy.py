import requests
from langchain.docstore.document import Document
from langchain.document_loaders.base import BaseLoader
from pyld import jsonld
import json



doc = {
    "http://schema.org/name": "Manu Sporny",
    "http://schema.org/url": {"@id": "http://manu.sporny.org/"},
    "http://schema.org/image": {"@id": "http://manu.sporny.org/images/manu.png"}
}

context = {
    "name": "http://schema.org/name",
    "homepage": {"@id": "http://schema.org/url", "@type": "@id"},
    "image": {"@id": "http://schema.org/image", "@type": "@id"}
}

# compact a document according to a particular context
# see: https://json-ld.org/spec/latest/json-ld/#compacted-document-form
compacted = jsonld.compact(doc, context)

print(json.dumps(compacted, indent=2))








class JSONDocumentLoader(BaseLoader):
    def __init__(self, url: str, headers: dict):
        self.url = url
        self.headers = headers

    def load(self) -> list[Document]:
        response = requests.get(self.url, headers=self.headers)
        json_data = response.json()
        expanded = jsonld.expand(json_data)

        print(json.dumps(expanded, indent=2))
        documents = self.parse(json_data)
      
        return documents

    def parse(self, json_data) -> list[Document]:
        documents = []
        for item in json_data:
            document = Document(
                metadata={
                    # Set the metadata properties based on the JSON data
                    # Example:
                    "source": self.url,
                    # ...
                },
                pageContent=item["content"],  # Set the page content based on the JSON data
            )
            documents.append(document)
        return documents
    
loader = JSONDocumentLoader("https://spoggy-test2.solidcommunity.net/public/", {
    # "Authorization": "Bearer <token>",
'Accept': 'application/ld+json',
})

#documents = loader.load()


# jsonld.set_document_loader(jsonld.aiohttp_document_loader(timeout=...))

flattened = jsonld.flatten('https://spoggy-test3.solidcommunity.net/public/')
print(json.dumps(flattened, indent=2))

for i in flattened:
    print (i['@id'], "\t",i['@type'] )
