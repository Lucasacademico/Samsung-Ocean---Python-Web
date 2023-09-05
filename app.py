# Importando a biblioteca flask
from flask import Flask
from flask import render_template

app = Flask("meu app")

posts = [
    {
        "titulo":"Minha primeira postagem",
        "texto":"teste"
    },
    {
        "titulo":"Segunda primeira postagem",
        "texto":"Outroteste"
    }
]

@app.route('/')
def exibir_entradas():
    entradas = posts # MOCK das postagens
    return render_template('exibir_entradas.html', entradas=entradas)

