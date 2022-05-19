from databaseApi import app
from flask import Response, render_template
import json
from flask_cors import CORS, cross_origin

cors = CORS(app, resources={r"/foo": {"origins": "http://localhost:port"}})
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def Index():
    return render_template('index.html')


def Tupple_to_json(obj,json,coltitle):
    OrcNum = len(obj)
    for item in range(OrcNum):
        dict_ = dict(zip(coltitle, obj[item]))
        json.append(dict_)


def gera_response(status, conteudo, mensagem=False):
    body = {}
    body = conteudo

    if(mensagem):
        body["mensagem"] = mensagem

    return Response(json.dumps(body), status=status, mimetype="application/json")