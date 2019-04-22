# Consulta de Nota fiscal
#
# Atenção: Somente é permitido consultar a chave da nota fiscal emitida pelo
# emissor da WebmaniaBR, não sendo possível consultar nota fiscal de terceiro
# ou emitida em outro sistema.

# Biblioteca de comunicação http/https
import http.client
import json

# Busca o arquivo que contém o json para Consulta de Nota Fiscal
with open('ExemploJson/consultarNotaFiscal.json', 'r') as json_file:
   # Carrega o conteudo do arquivo e converte em array
   array = json.load(json_file)

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

# Comunicação com a API
conn.request("GET", "/api/1/nfe/consulta/?chave="+array['chave']+"&ambiente="+array['ambiente'], headers=headers)

# Retorno da API
res = conn.getresponse()
data = res.read()

# Exibir retorno
print(data.decode("utf-8"))
