import sys
from datetime import datetime

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))
if len(sys.argv) == 1:
    print("try `python solid.py https://spoggy-test5.solidcommunity.net/public/`")
    exit()

url = str(sys.argv[1])
print(url)

urls = []


class SolidScanner():
    def __init__(self, url: str):
        self.url = url
        dt = datetime.now()

        # getting the timestamp
        ts = datetime.timestamp(dt)
        print("scanning ", url)
        resource = {"url": url, "start": ts}
        urls.append(resource)
        self.__scan__()

    def __scan__(self):
        """  print(urls)
          available =  list(filter(lambda x: 'start' in x and 'pending' not in x , urls))
          print(available)"""
        if len(urls) > 0:
            url = urls.pop()
            print("url", url)


scanner = SolidScanner(url)
