from ProxyService import ProxyService

p = ProxyService(limit=100)

proxy = p.getProxy()
print(proxy)