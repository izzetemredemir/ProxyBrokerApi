# ProxyBrokerApi
ProxyBrokerApi is an api service for ProxyBroker. It provides checked http-https proxies. It returns every time different proxy 
and keeps them in used-proxies.txt It uses Python3.6 + ProxyBroker , Flast-restful api .

## Features
ProxyBrokerApi provides every-time different http-https proxy.
This proxies are checked and fresh proxies are stored in proxies.txt 
Used proxies are stored in used-proxies.txt .
You can clear this txt files from api.

## Requirements

* Python 3.6+

* [ProxyBroker](https://github.com/constverum/ProxyBroker)

* Flask-RESTful

## ProxyBroker 
ProxyBroker is very useful tool .It finds and checks proxies from public pools. 
You can check their website for extra information  [proxybroker.readthedocs.io](proxybroker.readthedocs.io)

## Usage
### Api Examples 

#### Get a Proxy

[ApiTester.py](https://github.com/izzetemredemir/ProxyBrokerApi/blob/master/example/ApiTester.py)
| PATH    | Request Type| Post  |Desc  |
| :---         |     :---:      |         :---:      | ---: |
|/         | GET    |   |  Return a proxy |

```python
import requests

url = 'http://127.0.0.1:5000/'

r = requests.post(url)

print(r.text);
```
This code will return an unique proxy or you can visit http://127.0.0.1:5000/  directly from browser.

#### Clear .txt files
[ApiClearTester.py](https://github.com/izzetemredemir/ProxyBrokerApi/blob/master/example/ApiClearTester.py)

| PATH    | Request Type| Post  | Desc  |
| :---         |     :---:      |          :---:      |     ---: |
|/cmd          | POST     | {'clear': 'all'}   | Clar all txt files|
|/cmd         | POST       | {'clear': 'used_proxies'}    | clear used_proxies.txt|
|/cmd         | POST       | {'clear': 'proxies'}   |clear  proxies.txt|
```python
import requests

url = 'http://127.0.0.1:5000/cmd'

command = {'clear': 'all'} # It clears  used_prixies.txt and clears proxies.txt
#command = {'clear': 'used_proxies'} #  It clears used_prixies.txt
#command = {'clear': 'proxies'}      # It clears proxies.txt

x = requests.post(url, json = command)

print(x.text)
```

ProxyBrokerApi uses txt files for stroing proxies. proxies.txt stores new proxies. used-proxies.txt stores used proxies.
You can clear this txt files from api .


# Türkçe
ProxyBrokerApi ProxyBroker adlı aracı kullanarak her seferinde farklı ve kontrol edilmiş bir proxy veren bir araçtır. 
Daha önceden kullandığı proxyleri used-proxies.txt de saklar yeni olanları ise proxies.txt de saklar.

ProxyApi.py dosyasını çalıştırdığınız zaman Flask http://127.0.0.1:5000/ adresinden isteklerinize cevap verecektir.
Direk http://127.0.0.1:5000/ e istek attığınızda size proxyi json formatında geri döner.

Txt dosylarını bazen temizlemeniz gerekebilir bunu api üzerinden yapabilirsiniz bunun için  http://127.0.0.1:5000/cmd adresine 
post olarak istek atmanız gerekiyor örneğin  command = {'clear': 'all'}  her iki dosyayıda temizler. 

Bu api servisini localde kullanmak için tasarladım her birinde  farklı ip adresine ihtiyaç duyabileceğiniz birden fazla servisiniz var ise
böyle bir api servisine ihtiyacınız olabilir. 


### License
Licensed under the Apache License, Version 2.0
