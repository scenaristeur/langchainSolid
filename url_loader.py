from langchain.document_loaders import WebBaseLoader


#loader = WebBaseLoader("https://github.com/basecamp/handbook/blob/master/37signals-is-you.md")

loader = WebBaseLoader("https://spoggy-test2.solidcommunity.net/public/")


docs = loader.load()

print(docs[0].page_content[:500])