### add your openai api key in .env

`cp .env.example .env` and complete .env


### install dependencies 
on windows you need Microsoft Visual C++ 14.0 or greater https://visualstudio.microsoft.com/fr/visual-cpp-build-tools/
https://github.com/chroma-core/chroma/issues/189#issuecomment-1454418844

` pip install -r requirements.txt`

### run this tool for scanning a pod
`python solid.py https://spoggy-test5.solidcommunity.net/public/`


### asking a question
`python solid_question.py`



# tuto
- https://learn.deeplearning.ai/langchain-chat-with-your-data/lesson/2/document-loading




 - json loader https://www.youtube.com/watch?v=Ldr-ioU_ELo

 # langchain api reference 
 - https://github.com/hwchase17/langchain/blob/9b615022e2b6a3591347ad77a3e21aad6cf24c49/docs/api_reference/api_reference.rst#L595

 ### clean db 
  be carefull !rm -rf ./docs/chroma  # remove old database files if any

