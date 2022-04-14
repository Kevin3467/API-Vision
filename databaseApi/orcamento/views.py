from flask import request, Blueprint
import json
from databaseApi import db
from databaseApi.main import gera_response
from databaseApi.models import Ctrl_orcamentos
from flask_jwt_extended import jwt_required

orcamento = Blueprint('orcamento', __name__)


@orcamento.route('/read/orcamentos', methods=['GET'])
def Orcamento():

    orcamento_obj = Ctrl_orcamentos.query.all()
    orcamento_json = [orcamento.to_json() for orcamento in orcamento_obj]


    return gera_response(200,orcamento_json)