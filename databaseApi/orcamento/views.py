from flask import Blueprint
from databaseApi import db
from databaseApi.main import gera_response, cross_origin, Tupple_to_json
from databaseApi.models import Ctrl_orcamentos, Ctrl_chamados, Ctrl_contrato, Ctrl_coordenadores
from flask_jwt_extended import jwt_required

orcamento = Blueprint('orcamento', __name__)
    

    

@orcamento.route('/read/orcamentos', methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
@jwt_required()
def Orcamento():

    orcamento_obj = db.session.query(
        Ctrl_orcamentos.orcnome, Ctrl_orcamentos.orcdescricao, Ctrl_orcamentos.orccodigo, Ctrl_chamados.id, Ctrl_contrato.id,Ctrl_orcamentos.id,
        Ctrl_chamados.chmEntrada, Ctrl_contrato.cntNome, Ctrl_coordenadores.codNome, Ctrl_coordenadores.codEmpresa
        ).filter(
        Ctrl_orcamentos.idchamado == Ctrl_chamados.id,
        Ctrl_chamados.idcnt == Ctrl_contrato.id,
        Ctrl_chamados.idCoordenador == Ctrl_coordenadores.id
        ).all()
    orcamento_json = []
    colunas = ('Nome','Descrição','Codigo','idchamado','idcontrato','id','dataEntrada','contrato','Coordenador','empresa')
    Tupple_to_json(orcamento_obj,orcamento_json,colunas)

    return gera_response(200, orcamento_json)