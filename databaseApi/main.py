from databaseApi import app
from flask import Response, render_template
import json


@app.route('/')
def Index():
    return render_template('index.html')

def gera_response(status, nome_do_conteudo, conteudo, mensagem=False):
    body = {}
    body[nome_do_conteudo] = conteudo

    if(mensagem):
        body["mensagem"] = mensagem

    return Response(json.dumps(body), status=status, mimetype="application/json")