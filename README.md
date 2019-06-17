# PyPegaCEPs
Retorna os dados completos dos endereços a partir de uma lista de logradouros utilizando Python.


### Como rodar o projeto?
* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Adicione sua lista em `entorno_list.py`
* Altere a UF e Cidade de acordo com sua lista de logradouros em `app.py`
`resp = pega_cep(f'SP/Santo André/{endereco}')`
* Rode a aplicação

```
git clone https://github.com/tiagocordeiro/pypegaceps.git
cd pypegaceps
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python app.py
```

Pronto, um arquivo `enderecos_completos.csv` será gerado.


### Como gerar uma lista de logradouros?
* Acesse http://overpass-turbo.eu/
* Selecione uma área no mapa e clique em `Executar`.
* Substitua a lista gerada no arquivo `entorno_list.py`, 
não esqueça de alterar a UF e Cidade no arquivo `app.py`.
