# ProxyBrokerApi

A small local Flask API that hands out a different, checked HTTP or HTTPS proxy on every request. It uses [ProxyBroker](https://github.com/constverum/ProxyBroker) to find and check proxies from public sources, and is meant for setups where several local services each need a different IP address.

> **Status:** archived. Built in 2020. Kept for reference, not maintained.

## What it does

- Returns one proxy per request as JSON, for example `{"proxy": "http://203.0.113.10:8080"}`.
- Never hands out the same proxy twice: each proxy it serves is removed from `proxies.txt` and recorded in `used-proxies.txt`.
- When `proxies.txt` runs out, runs a new ProxyBroker search for HTTP and HTTPS proxies and refills the file. The search limit starts at 10 and grows by 100 before every refill.
- Clears `proxies.txt`, `used-proxies.txt` or both through a command endpoint.
- `ProxyService.py` also works on its own, without the API (see [example/ProxyServiceTester.py](example/ProxyServiceTester.py)).

## API

| Path   | Method      | Body                         | Description                                   |
| ------ | ----------- | ---------------------------- | --------------------------------------------- |
| `/`    | GET or POST |                              | Returns an unused proxy                       |
| `/cmd` | POST        | `{"clear": "all"}`           | Clears `proxies.txt` and `used-proxies.txt`   |
| `/cmd` | POST        | `{"clear": "proxies"}`       | Clears `proxies.txt`                          |
| `/cmd` | POST        | `{"clear": "used_proxies"}`  | Clears `used-proxies.txt`                     |

Get a proxy ([example/ApiTester.py](example/ApiTester.py)):

```python
import requests

url = 'http://127.0.0.1:5000/'

r = requests.post(url)

print(r.text)
```

You can also open http://127.0.0.1:5000/ in a browser.

Clear the files ([example/ApiClearTester.py](example/ApiClearTester.py)):

```python
import requests

url = 'http://127.0.0.1:5000/cmd'

command = {'clear': 'all'}             # clears used-proxies.txt and proxies.txt
# command = {'clear': 'used_proxies'}  # clears used-proxies.txt
# command = {'clear': 'proxies'}       # clears proxies.txt

x = requests.post(url, json=command)

print(x.text)
```

## Tech stack

- Python 3 (the original target was Python 3.6+)
- Flask
- [ProxyBroker](https://proxybroker.readthedocs.io) (asyncio based proxy finder and checker)
- requests (examples only)

## Running it locally

```bash
pip install Flask proxybroker
python ProxyApi.py
```

The API answers on http://127.0.0.1:5000/. On startup it fetches one proxy, so with an empty `proxies.txt` it runs a ProxyBroker search before the server comes up.

- `requeriments.txt` is a full export of a 2020 Anaconda environment, not a minimal list. The code itself only imports Flask and ProxyBroker (plus requests in the examples).
- The latest ProxyBroker release on PyPI (0.3.2, from 2019) lists Python 3.5 and 3.6 as supported, so a newer Python may need changes.
- The app runs Flask with `debug=True`. Keep it on localhost.

## License

GPL-3.0, see [LICENSE](LICENSE).
