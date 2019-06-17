import csv
import json

import requests

from entorno_list import enderecos


def pega_cep(logradouro):
    url_api = f'http://www.viacep.com.br/ws/{logradouro}/json'
    req = requests.get(url_api)
    if req.status_code == 200:
        dados_json = json.loads(req.text)
        return dados_json


with open('enderecos_completos.csv', mode='w') as enderecos_completos:
    enderecos_writer = csv.writer(enderecos_completos, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    enderecos_writer.writerow(['CEP', 'Logradouro', 'Bairro', 'Complemento', 'Localidade', 'UF'])

    for endereco in enderecos.split("\n"):
        resp = pega_cep(f'SP/Santo André/{endereco}')  # Altere a UF e Cidade de acordo com sua lista de logradouros
        for _ in range(len(resp)):
            enderecos_writer.writerow([f'{resp[_]["cep"]}', f'{resp[_]["logradouro"]}', f'{resp[_]["bairro"]}',
                                       f'{resp[_]["complemento"]}', f'{resp[_]["localidade"]}', f'{resp[_]["uf"]}'])
            print(endereco)
