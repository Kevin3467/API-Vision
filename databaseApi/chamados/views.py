from flask import Blueprint
from databaseApi import db
from databaseApi.main import gera_response, cross_origin, Tupple_to_json
from databaseApi.models import Ctrl_chamados
from flask_jwt_extended import jwt_required

chamados = Blueprint('chamados', __name__)

# lista todos os chamados na tabela
@chamados.route('/read/chamados', methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
@jwt_required()
def Chamados():
    
    Chamados_obj = Ctrl_chamados.query.all()
    Chamados_json = [chamado.to_json() for chamado in Chamados_obj]
    

    return gera_response(200, Chamados_json)