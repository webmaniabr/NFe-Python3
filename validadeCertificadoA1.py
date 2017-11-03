import http.client

conn = http.client.HTTPSConnection("webmaniabr.com")

headers = {
    'cache-control': "no-cache",
    'content-type': "application/json",
    'x-consumer-key': "SEU_CONSUMER_KEY",
    'x-consumer-secret': "SEU_CONSUMER_SECRET",
    'x-access-token': "SEU_ACCESS_TOKEN",
    'x-access-token-secret': "SEU_ACCESS_TOKEN_SECRET"
}

conn.request("GET", "/api/1/nfe/certificado/", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
