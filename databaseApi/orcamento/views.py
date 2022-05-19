from flask import request, Blueprint
from databaseApi import db
from databaseApi.main import gera_response, cross_origin
from databaseApi.models import Ctrl_orcamentos
from flask_jwt_extended import jwt_required

orcamento = Blueprint('orcamento', __name__)



def Tupple_to_json(obj,json):
    OrcNum = len(obj)
    for item in range(OrcNum):
        dict_ = dict(zip(('Nome','Descrição','Codigo'), obj[item]))
        json.append(dict_)
    

    

@orcamento.route('/read/orcamentos', methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
@jwt_required()
def Orcamento():

    orcamento_obj = db.session.query(Ctrl_orcamentos.orcnome, Ctrl_orcamentos.orcdescricao, Ctrl_orcamentos.orccodigo).all()
    orcamento_json = []
    Tupple_to_json(orcamento_obj,orcamento_json)

    return gera_response(200, orcamento_json)