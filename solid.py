import sys
from datetime import datetime
from JSONDocumentLoader import JSONDocumentLoader
from termcolor import colored

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))
if len(sys.argv) == 1:
    print("try `python solid.py https://spoggy-test5.solidcommunity.net/public/`")
    exit()

url = str(sys.argv[1])
print(url)

urls = []
urls_scanned = []


class SolidScanner():
    def __init__(self, url: str):
        self.url = url
        dt = datetime.now()
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
            print("rest", urls)
            loader = JSONDocumentLoader(url)
            # docs = loader.load()
            loaded = loader.load()
            if ("error" in loaded):
                print("############################ERROR", loaded["error"])
            else:
                docs = loaded["documents"]
                containers = loaded["containers"]
                print("\ndocs", len(docs), "loaded")
                print("containers", len(containers))
                dt = datetime.now()
                print("&&& ", url)
                url['end'] = datetime.timestamp(dt)

                urls_scanned.append(url)
                self.__storeDocs__(docs)
                self.__scanContainers__(containers)
            print(str(len(urls_scanned)) +
                  " scanned,\t"+str(len(urls))+" pending")

    def __scanContainers__(self, containers):
        for container in containers:
            found = False
            for scanned in urls_scanned:
                # print("àà", scanned['url'])
                if (container == scanned['url']):
                    found = True
                    break
            print("__is already scanned ?", container, found)
            if (found == False):
                dt = datetime.now()
                ts = datetime.timestamp(dt)
                resource = {"url": container, "start": ts}
                urls.append(resource)
                self.__scan__()

                # if key in dict and dict[key] != value:
               # dict[key]=value
               # urls.append(resource)
        # s#elf.__scan__()

    def __storeDocs__(self, docs):
        #print("__storing", docs)
        print(colored('__storing docs', 'red'), colored(len(docs), 'green'))


scanner = SolidScanner(url)
