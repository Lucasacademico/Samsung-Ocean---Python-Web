
# Importando a biblioteca flask
from flask import Flask 

# Criar app
app = Flask("meu app")

# # Criando rota pra linkar o caminho com a função  hello
# @app.route('/')
# def hello():
#     return "Hello World"

@app.route('/novo')
def hello():
	return "<h1>Nova Página</h1>"
    # Ao rodar essa nova rota, na url, digitar " /novo "
