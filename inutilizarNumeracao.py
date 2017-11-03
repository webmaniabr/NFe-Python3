'''
JSON request:

{
  "sequencia": "101-109",
  "motivo": "Inutilização por problemas técnicos.",
  "ambiente": "1",
  "serie": "99",
  "modelo": "1"
}
'''

import http.client

conn = http.client.HTTPSConnection("webmaniabr.com")

payload = "{\"sequencia\":\"101-109\",\"motivo\":\"Inutilização por problemas técnicos.\",\"ambiente\":\"1\",\"serie\":\"99\",\"modelo\":\"1\"}"

headers = {
    'cache-control': "no-cache",
    'content-type': "application/json",
    'x-consumer-key': "SEU_CONSUMER_KEY",
    'x-consumer-secret': "SEU_CONSUMER_SECRET",
    'x-access-token': "SEU_ACCESS_TOKEN",
    'x-access-token-secret': "SEU_ACCESS_TOKEN_SECRET"
}

conn.request("PUT", "/api/1/nfe/inutilizar/", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
