'''
JSON request:

{
  "chave":"45150819652219000198550990000000011442380343",
  "correcao":"O CFOP correto é 5.102 referente a revenda tributada no mesmo estado.",
  "ambiente":1
}
'''

import http.client

conn = http.client.HTTPSConnection("webmaniabr.com")

payload = "{\"chave\": \"45150819652219000198550990000000011442380343\",\"correcao\": \"O CFOP correto é 5.102 referente a revenda tributada no mesmo estado.\",\"ambiente\": \"1\"}"

headers = {
    'cache-control': "no-cache",
    'content-type': "application/json",
    'x-consumer-key': "SEU_CONSUMER_KEY",
    'x-consumer-secret': "SEU_CONSUMER_SECRET",
    'x-access-token': "SEU_ACCESS_TOKEN",
    'x-access-token-secret': "SEU_ACCESS_TOKEN_SECRET"
}

conn.request("POST", "/api/1/nfe/cartacorrecao/", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
