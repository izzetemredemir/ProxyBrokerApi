import asyncio
from proxybroker import Broker
import os

class ProxyService():

    def __init__(self, limit=None ,filename='proxies.txt'):
        self.limit = limit
        self.filename = filename

    async def save(self,proxies, filename):
        """Save proxies to a file."""
        with open(filename, 'w') as f:
            while True:
                proxy = await proxies.get()
                if proxy is None:
                    break
                proto = 'https' if 'HTTPS' in proxy.types else 'http'
                row = '%s://%s:%d\n' % (proto, proxy.host, proxy.port)
                f.write(row)


    def proxy_saver(self):
        proxies = asyncio.Queue()
        broker = Broker(proxies)
        tasks = asyncio.gather(
            broker.find(types=['HTTP', 'HTTPS'], limit=self.limit),
            self.save(proxies, filename=self.filename),
        )
        loop = asyncio.get_event_loop()
        loop.run_until_complete(tasks)

    def clear_used_proxies(self):
        file = open("used-proxies.txt", "w").close()
    def clear_proxies(self):
        file = open(self.filename, "w").close()

    def clear_all(self):
        open("used-proxies.txt", "w").close()
        open(self.filename, "w").close()

    def file_remover(self,i):
        fin = open(self.filename, "rt")
        data = fin.read()
        data = data.replace(i, '')
        fin.close()

        fin = open(self.filename, "wt")
        fin.write(data)
        fin.close()

    # It extends proxies list
    def proxy_reflesher(self):
        self.limit +=100
        self.proxy_saver()

    #file_chekcer return true if file is empty else it will return true
    def file_checker(self,file):

        if os.stat(file).st_size == 0:
            return True
        else:
            return False

    def getProxy_toFile(self):
        try:
            proxyFile = open(self.filename, "r+")
        except:
            open(self.filename, "w").close()
            proxyFile = open(self.filename, "r+")
        try :
            usedFile = open("used-proxies.txt", "r+")
        except:
            open("used-proxies.txt", "w").close()
            usedFile = open("used-proxies.txt", "r+")

        usedList = usedFile.readlines()
        data = proxyFile.readlines()
        proxyFile.close()
        for i in data:
            if any(i in s for s in usedList):
                 self.file_remover(i)
            else:
                usedFile.write(i)
                usedFile.close()
                self.file_remover(i)
                return i

    def proxy_replacer(self,proxy):
        proxy = proxy.replace("\n", '')
        return proxy

    def getProxy(self):
        proxy = self.getProxy_toFile()
        if proxy == None:
            self.proxy_reflesher()
            proxy = self.getProxy_toFile()
            return self.proxy_replacer(proxy)
        else:
            return self.proxy_replacer(proxy)


def main():
    p = ProxyService(limit=10)
    print(p.getProxy())

if __name__ == '__main__':
   main()