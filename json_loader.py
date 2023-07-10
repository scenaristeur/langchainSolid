#!pip install jq

from langchain.document_loaders import JSONLoader

import json
from pathlib import Path
from pprint import pprint


file_path='https://spoggy-test2.solidcommunity.net/public/'
data = json.loads(Path(file_path).read_text())