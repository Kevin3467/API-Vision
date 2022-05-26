from flask import Blueprint
from databaseApi import db
from databaseApi.main import gera_response, cross_origin, Tupple_to_json
from databaseApi.models import Ctrl_chamados,Ctrl_contrato
from flask_jwt_extended import jwt_required

chamados = Blueprint('chamados', __name__)



# lista todos os chamados na tabela
@chamados.route('/read/chamados/<idcnt>', methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
@jwt_required()
def Chamados(idcnt):
    
    Chamados_obj = db.session.query(
        Ctrl_chamados.id, Ctrl_contrato.id, Ctrl_chamados.chmTitulo
        ).filter(
        Ctrl_chamados.idcnt == Ctrl_contrato.id,
        Ctrl_contrato.id == idcnt
        ).all()

    cols_title = ('id','idcnt','Titulo')
    Chamados_json = []
    Tupple_to_json(Chamados_obj,Chamados_json,cols_title)
    

    return gera_response(200, Chamados_json)