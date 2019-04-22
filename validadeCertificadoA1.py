# Biblioteca de comunicação http/https
import http.client

#  Define o Host para a comunicação com a API
conn = http.client.HTTPSConnection("webmaniabr.com")

# Credenciais de acesso
headers = {
    'cache-control': "no-cache",
    'content-type': "application/json",
    'x-consumer-key': "SEU_CONSUMER_KEY",
    'x-consumer-secret': "SEU_CONSUMER_SECRET",
    'x-access-token': "SEU_ACCESS_TOKEN",
    'x-access-token-secret': "SEU_ACCESS_TOKEN_SECRET"
}

# Comunicando com a API
conn.request("GET", "/api/1/nfe/certificado/", headers=headers)

# Retorno da API
res = conn.getresponse()
data = res.read()

# Exibir retorno
print(data.decode("utf-8"))
