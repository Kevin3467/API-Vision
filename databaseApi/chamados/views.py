from turtle import title
from flask import Blueprint, request
from databaseApi import db
from databaseApi.main import gera_response, cross_origin, Tupple_to_json
from databaseApi.models import Ctrl_chamados,Ctrl_contrato
from sqlalchemy import or_
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


# lista todos os chamados na tabela
@chamados.route('/read/chamados/bmsa', methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
@jwt_required()
def Chamados_bmsa():
    
    Chamados_obj = db.session.query(
        Ctrl_chamados.id, Ctrl_contrato.id, Ctrl_chamados.chmTitulo
        ).filter(
        Ctrl_chamados.idcnt == Ctrl_contrato.id,
        or_(Ctrl_contrato.id == 6, Ctrl_contrato.id == 7)
        ).all()

    cols_title = ('id','idcnt','Titulo')
    Chamados_json = []
    Tupple_to_json(Chamados_obj,Chamados_json,cols_title)
    

    return gera_response(200, Chamados_json)





@chamados.route('/create/chamados', methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
@jwt_required()
def create_chamados():
        cntid = request.json.get('cntid', None)
        slct = request.json.get('slct', None)
        desc = request.json.get('desc', None)
        cltid = request.json.get('cltid', None)
        crdid = request.json.get('crdid', None)
        title = request.json.get('title', None)
        
        if not cntid:
            return 'Missing cntid', 400
        if not slct:
            return 'Missing slct', 400
        if not desc:
            return 'Missing desc', 400
        if not cltid:
            return 'Missing cltid', 400
        if not crdid:
            return 'Missing crdid', 400
        if not title:
            return 'Missing title', 400


        newChamado = Ctrl_chamados(
            idcnt=cntid,
            chmSolicitacao=slct,
            chmDescricao=desc,
            idClientes=cltid,
            idCoordenador=crdid,
            chmTitulo=title
            )
        db.session.add(newChamado)
        db.session.commit()

        return "chamado criado com sucesso", 200