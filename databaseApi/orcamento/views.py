from flask import Blueprint, request
from databaseApi import db
from databaseApi.main import gera_response, cross_origin, Tupple_to_json
from databaseApi.models import Ctrl_orcamentos, Ctrl_chamados, Ctrl_contrato, Ctrl_coordenadores
from sqlalchemy import or_
from flask_jwt_extended import jwt_required

orcamento = Blueprint('orcamento', __name__)


@orcamento.route('/create/orcamento', methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
@jwt_required()
def create_orcamento():
        orcnome = request.json.get('orcnome', None)
        orcdesc = request.json.get('orcdesc', None)
        orccod = request.json.get('orccod', None)
        chmid = request.json.get('chmid', None)
        orcstatus = request.json.get('orcstatus', None)
        
        if not orcnome:
            return 'Missing orcnome', 400
        if not orcdesc:
            return 'Missing orcdesc', 400
        if not chmid:
            return 'Missing chmid', 400
        if not orcstatus:
            return 'Missing orcstatus', 400


        newOrcamento = Ctrl_orcamentos(
            orcnome=orcnome,
            orcdescricao=orcdesc,
            orccodigo=orccod,
            orcstatus=orcstatus,
            idchamado=chmid,
            )
        db.session.add(newOrcamento)
        db.session.commit()

        return "Orcamento criado com sucesso", 200



@orcamento.route('/read/orcamentos', methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
@jwt_required()
def Orcamento():

    orcamento_obj = db.session.query(
        Ctrl_orcamentos.orcnome, Ctrl_orcamentos.orcdescricao, Ctrl_orcamentos.orccodigo, Ctrl_chamados.id, Ctrl_contrato.id,Ctrl_orcamentos.id,
        Ctrl_chamados.chmEntrada, Ctrl_contrato.cntNome, Ctrl_coordenadores.codNome, Ctrl_coordenadores.codEmpresa, Ctrl_orcamentos.orcstatus
        ).filter(
        Ctrl_orcamentos.idchamado == Ctrl_chamados.id,
        Ctrl_chamados.idcnt == Ctrl_contrato.id,
        Ctrl_chamados.idCoordenador == Ctrl_coordenadores.id
        ).all()
    orcamento_json = []
    colunas = ('Nome','Descrição','Codigo','idchamado','idcontrato','id','dataEntrada','contrato','Coordenador','empresa','status')
    Tupple_to_json(orcamento_obj,orcamento_json,colunas)

    return gera_response(200, orcamento_json)
#
#
#
# todos os filtros do porto Ferrovia
#
#
#
@orcamento.route('/read/orcamentos/portof/pendente', methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
@jwt_required()
def Orcamento_filtro_PF_pendente():

    orcamento_obj = db.session.query(
        Ctrl_orcamentos.orcnome, Ctrl_orcamentos.orcdescricao, Ctrl_orcamentos.orccodigo, Ctrl_chamados.id, Ctrl_contrato.id,Ctrl_orcamentos.id,
        Ctrl_chamados.chmEntrada, Ctrl_contrato.cntNome, Ctrl_coordenadores.codNome, Ctrl_coordenadores.codEmpresa
        ).filter(
        Ctrl_orcamentos.idchamado == Ctrl_chamados.id,
        Ctrl_chamados.idcnt == Ctrl_contrato.id,
        Ctrl_chamados.idCoordenador == Ctrl_coordenadores.id,
        Ctrl_contrato.cntNome == 'porto Ferrovia',
        Ctrl_orcamentos.orcstatus == 'pendente'
        ).all()
    orcamento_json = []
    colunas = ('Nome','Descrição','Codigo','idchamado','idcontrato','id','dataEntrada','contrato','Coordenador','empresa')
    Tupple_to_json(orcamento_obj,orcamento_json,colunas)

    return gera_response(200, orcamento_json)




@orcamento.route('/read/orcamentos/portof/aguardando', methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
@jwt_required()
def Orcamento_filtro_PF_aguardando():

    orcamento_obj = db.session.query(
        Ctrl_orcamentos.orcnome, Ctrl_orcamentos.orcdescricao, Ctrl_orcamentos.orccodigo, Ctrl_chamados.id, Ctrl_contrato.id,Ctrl_orcamentos.id,
        Ctrl_chamados.chmEntrada, Ctrl_contrato.cntNome, Ctrl_coordenadores.codNome, Ctrl_coordenadores.codEmpresa
        ).filter(
        Ctrl_orcamentos.idchamado == Ctrl_chamados.id,
        Ctrl_chamados.idcnt == Ctrl_contrato.id,
        Ctrl_chamados.idCoordenador == Ctrl_coordenadores.id,
        Ctrl_contrato.cntNome == 'porto Ferrovia',
        Ctrl_orcamentos.orcstatus == 'aguardando'
        ).all()
    orcamento_json = []
    colunas = ('Nome','Descrição','Codigo','idchamado','idcontrato','id','dataEntrada','contrato','Coordenador','empresa')
    Tupple_to_json(orcamento_obj,orcamento_json,colunas)

    return gera_response(200, orcamento_json)




@orcamento.route('/read/orcamentos/portof/liberado', methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
@jwt_required()
def Orcamento_filtro_PF_liberado():

    orcamento_obj = db.session.query(
        Ctrl_orcamentos.orcnome,
        Ctrl_orcamentos.orcdescricao,
        Ctrl_orcamentos.orccodigo,
        Ctrl_chamados.id,
        Ctrl_contrato.id,
        Ctrl_orcamentos.id,
        Ctrl_chamados.chmEntrada,
        Ctrl_contrato.cntNome,
        Ctrl_coordenadores.codNome,
        Ctrl_coordenadores.codEmpresa
        ).filter(
        Ctrl_orcamentos.idchamado == Ctrl_chamados.id,
        Ctrl_chamados.idcnt == Ctrl_contrato.id,
        Ctrl_chamados.idCoordenador == Ctrl_coordenadores.id,
        Ctrl_contrato.cntNome == 'porto Ferrovia',
        Ctrl_orcamentos.orcstatus == 'liberado'
        ).all()
    orcamento_json = []
    colunas = ('Nome','Descrição','Codigo','idchamado','idcontrato','id','dataEntrada','contrato','Coordenador','empresa')
    Tupple_to_json(orcamento_obj,orcamento_json,colunas)

    return gera_response(200, orcamento_json)




@orcamento.route('/read/orcamentos/portof/cancelado', methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
@jwt_required()
def Orcamento_filtro_PF_cancelado():

    orcamento_obj = db.session.query(
        Ctrl_orcamentos.orcnome, Ctrl_orcamentos.orcdescricao, Ctrl_orcamentos.orccodigo, Ctrl_chamados.id, Ctrl_contrato.id,Ctrl_orcamentos.id,
        Ctrl_chamados.chmEntrada, Ctrl_contrato.cntNome, Ctrl_coordenadores.codNome, Ctrl_coordenadores.codEmpresa
        ).filter(
        Ctrl_orcamentos.idchamado == Ctrl_chamados.id,
        Ctrl_chamados.idcnt == Ctrl_contrato.id,
        Ctrl_chamados.idCoordenador == Ctrl_coordenadores.id,
        Ctrl_contrato.cntNome == 'porto Ferrovia',
        Ctrl_orcamentos.orcstatus == 'cancelado'
        ).all()
    orcamento_json = []
    colunas = ('Nome','Descrição','Codigo','idchamado','idcontrato','id','dataEntrada','contrato','Coordenador','empresa')
    Tupple_to_json(orcamento_obj,orcamento_json,colunas)

    return gera_response(200, orcamento_json)
    
#
#
#
# todos os filtros do porto manutenção
#
#
#
@orcamento.route('/read/orcamentos/portom/pendente', methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
@jwt_required()
def Orcamento_filtro_PM_pendente():

    orcamento_obj = db.session.query(
        Ctrl_orcamentos.orcnome, Ctrl_orcamentos.orcdescricao, Ctrl_orcamentos.orccodigo, Ctrl_chamados.id, Ctrl_contrato.id,Ctrl_orcamentos.id,
        Ctrl_chamados.chmEntrada, Ctrl_contrato.cntNome, Ctrl_coordenadores.codNome, Ctrl_coordenadores.codEmpresa
        ).filter(
        Ctrl_orcamentos.idchamado == Ctrl_chamados.id,
        Ctrl_chamados.idcnt == Ctrl_contrato.id,
        Ctrl_chamados.idCoordenador == Ctrl_coordenadores.id,
        Ctrl_contrato.cntNome == 'Porto Manutenção',
        Ctrl_orcamentos.orcstatus == 'pendente'
        ).all()
    orcamento_json = []
    colunas = ('Nome','Descrição','Codigo','idchamado','idcontrato','id','dataEntrada','contrato','Coordenador','empresa')
    Tupple_to_json(orcamento_obj,orcamento_json,colunas)
    print(orcamento_obj)

    return gera_response(200, orcamento_json)




@orcamento.route('/read/orcamentos/portom/aguardando', methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
@jwt_required()
def Orcamento_filtro_PM_aguardando():

    orcamento_obj = db.session.query(
        Ctrl_orcamentos.orcnome, Ctrl_orcamentos.orcdescricao, Ctrl_orcamentos.orccodigo, Ctrl_chamados.id, Ctrl_contrato.id,Ctrl_orcamentos.id,
        Ctrl_chamados.chmEntrada, Ctrl_contrato.cntNome, Ctrl_coordenadores.codNome, Ctrl_coordenadores.codEmpresa
        ).filter(
        Ctrl_orcamentos.idchamado == Ctrl_chamados.id,
        Ctrl_chamados.idcnt == Ctrl_contrato.id,
        Ctrl_chamados.idCoordenador == Ctrl_coordenadores.id,
        Ctrl_contrato.cntNome == 'porto manutenção',
        Ctrl_orcamentos.orcstatus == 'aguardando'
        ).all()
    orcamento_json = []
    colunas = ('Nome','Descrição','Codigo','idchamado','idcontrato','id','dataEntrada','contrato','Coordenador','empresa')
    Tupple_to_json(orcamento_obj,orcamento_json,colunas)

    return gera_response(200, orcamento_json)




@orcamento.route('/read/orcamentos/portom/liberado', methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
@jwt_required()
def Orcamento_filtro_PM_liberado():

    orcamento_obj = db.session.query(
        Ctrl_orcamentos.orcnome, Ctrl_orcamentos.orcdescricao, Ctrl_orcamentos.orccodigo, Ctrl_chamados.id, Ctrl_contrato.id,Ctrl_orcamentos.id,
        Ctrl_chamados.chmEntrada, Ctrl_contrato.cntNome, Ctrl_coordenadores.codNome, Ctrl_coordenadores.codEmpresa
        ).filter(
        Ctrl_orcamentos.idchamado == Ctrl_chamados.id,
        Ctrl_chamados.idcnt == Ctrl_contrato.id,
        Ctrl_chamados.idCoordenador == Ctrl_coordenadores.id,
        Ctrl_contrato.cntNome == 'porto manutenção',
        Ctrl_orcamentos.orcstatus == 'liberado'
        ).all()
    orcamento_json = []
    colunas = ('Nome','Descrição','Codigo','idchamado','idcontrato','id','dataEntrada','contrato','Coordenador','empresa')
    Tupple_to_json(orcamento_obj,orcamento_json,colunas)

    return gera_response(200, orcamento_json)




@orcamento.route('/read/orcamentos/portom/cancelado', methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
@jwt_required()
def Orcamento_filtro_PM_cancelado():

    orcamento_obj = db.session.query(
        Ctrl_orcamentos.orcnome, Ctrl_orcamentos.orcdescricao, Ctrl_orcamentos.orccodigo, Ctrl_chamados.id, Ctrl_contrato.id,Ctrl_orcamentos.id,
        Ctrl_chamados.chmEntrada, Ctrl_contrato.cntNome, Ctrl_coordenadores.codNome, Ctrl_coordenadores.codEmpresa
        ).filter(
        Ctrl_orcamentos.idchamado == Ctrl_chamados.id,
        Ctrl_chamados.idcnt == Ctrl_contrato.id,
        Ctrl_chamados.idCoordenador == Ctrl_coordenadores.id,
        Ctrl_contrato.cntNome == 'porto manutenção',
        Ctrl_orcamentos.orcstatus == 'cancelado'
        ).all()
    orcamento_json = []
    colunas = ('Nome','Descrição','Codigo','idchamado','idcontrato','id','dataEntrada','contrato','Coordenador','empresa')
    Tupple_to_json(orcamento_obj,orcamento_json,colunas)

    return gera_response(200, orcamento_json)
#
#
#
#
# todos os filtros do facilities
#
#
#
@orcamento.route('/read/orcamentos/facilities/pendente', methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
@jwt_required()
def Orcamento_filtro_facilities_pendente():

    orcamento_obj = db.session.query(
        Ctrl_orcamentos.orcnome, Ctrl_orcamentos.orcdescricao, Ctrl_orcamentos.orccodigo, Ctrl_chamados.id, Ctrl_contrato.id,Ctrl_orcamentos.id,
        Ctrl_chamados.chmEntrada, Ctrl_contrato.cntNome, Ctrl_coordenadores.codNome, Ctrl_coordenadores.codEmpresa
        ).filter(
        Ctrl_orcamentos.idchamado == Ctrl_chamados.id,
        Ctrl_chamados.idcnt == Ctrl_contrato.id,
        Ctrl_chamados.idCoordenador == Ctrl_coordenadores.id,
        Ctrl_contrato.cntNome == 'facilities',
        Ctrl_orcamentos.orcstatus == 'pendente'
        ).all()
    orcamento_json = []
    colunas = ('Nome','Descrição','Codigo','idchamado','idcontrato','id','dataEntrada','contrato','Coordenador','empresa')
    Tupple_to_json(orcamento_obj,orcamento_json,colunas)

    return gera_response(200, orcamento_json)




@orcamento.route('/read/orcamentos/facilities/aguardando', methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
@jwt_required()
def Orcamento_filtro_facilities_aguardando():

    orcamento_obj = db.session.query(
        Ctrl_orcamentos.orcnome, Ctrl_orcamentos.orcdescricao, Ctrl_orcamentos.orccodigo, Ctrl_chamados.id, Ctrl_contrato.id,Ctrl_orcamentos.id,
        Ctrl_chamados.chmEntrada, Ctrl_contrato.cntNome, Ctrl_coordenadores.codNome, Ctrl_coordenadores.codEmpresa
        ).filter(
        Ctrl_orcamentos.idchamado == Ctrl_chamados.id,
        Ctrl_chamados.idcnt == Ctrl_contrato.id,
        Ctrl_chamados.idCoordenador == Ctrl_coordenadores.id,
        Ctrl_contrato.cntNome == 'facilities',
        Ctrl_orcamentos.orcstatus == 'aguardando'
        ).all()
    orcamento_json = []
    colunas = ('Nome','Descrição','Codigo','idchamado','idcontrato','id','dataEntrada','contrato','Coordenador','empresa')
    Tupple_to_json(orcamento_obj,orcamento_json,colunas)

    return gera_response(200, orcamento_json)




@orcamento.route('/read/orcamentos/facilities/liberado', methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
@jwt_required()
def Orcamento_filtro_facilities_liberado():

    orcamento_obj = db.session.query(
        Ctrl_orcamentos.orcnome, Ctrl_orcamentos.orcdescricao, Ctrl_orcamentos.orccodigo, Ctrl_chamados.id, Ctrl_contrato.id,Ctrl_orcamentos.id,
        Ctrl_chamados.chmEntrada, Ctrl_contrato.cntNome, Ctrl_coordenadores.codNome, Ctrl_coordenadores.codEmpresa
        ).filter(
        Ctrl_orcamentos.idchamado == Ctrl_chamados.id,
        Ctrl_chamados.idcnt == Ctrl_contrato.id,
        Ctrl_chamados.idCoordenador == Ctrl_coordenadores.id,
        Ctrl_contrato.cntNome == 'facilities',
        Ctrl_orcamentos.orcstatus == 'liberado'
        ).all()
    orcamento_json = []
    colunas = ('Nome','Descrição','Codigo','idchamado','idcontrato','id','dataEntrada','contrato','Coordenador','empresa')
    Tupple_to_json(orcamento_obj,orcamento_json,colunas)

    return gera_response(200, orcamento_json)




@orcamento.route('/read/orcamentos/facilities/cancelado', methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
@jwt_required()
def Orcamento_filtro_facilities_cancelado():

    orcamento_obj = db.session.query(
        Ctrl_orcamentos.orcnome, Ctrl_orcamentos.orcdescricao, Ctrl_orcamentos.orccodigo, Ctrl_chamados.id, Ctrl_contrato.id,Ctrl_orcamentos.id,
        Ctrl_chamados.chmEntrada, Ctrl_contrato.cntNome, Ctrl_coordenadores.codNome, Ctrl_coordenadores.codEmpresa
        ).filter(
        Ctrl_orcamentos.idchamado == Ctrl_chamados.id,
        Ctrl_chamados.idcnt == Ctrl_contrato.id,
        Ctrl_chamados.idCoordenador == Ctrl_coordenadores.id,
        Ctrl_contrato.cntNome == 'facilities',
        Ctrl_orcamentos.orcstatus == 'cancelado'
        ).all()
    orcamento_json = []
    colunas = ('Nome','Descrição','Codigo','idchamado','idcontrato','id','dataEntrada','contrato','Coordenador','empresa')
    Tupple_to_json(orcamento_obj,orcamento_json,colunas)

    return gera_response(200, orcamento_json)
#
#
#
# todos os filtros do bmsa
#
#
#
@orcamento.route('/read/orcamentos/bmsa/pendente', methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
@jwt_required()
def Orcamento_filtro_bmsa_pendente():
    salobo = 'Industrial Salobo'
    sossego = 'Industrial Sossego'
    orcamento_obj = db.session.query(
        Ctrl_orcamentos.orcnome, Ctrl_orcamentos.orcdescricao, Ctrl_orcamentos.orccodigo, Ctrl_chamados.id, Ctrl_contrato.id,Ctrl_orcamentos.id,
        Ctrl_chamados.chmEntrada, Ctrl_contrato.cntNome, Ctrl_coordenadores.codNome, Ctrl_coordenadores.codEmpresa
        ).filter(
        Ctrl_orcamentos.idchamado == Ctrl_chamados.id,
        Ctrl_chamados.idcnt == Ctrl_contrato.id,
        Ctrl_chamados.idCoordenador == Ctrl_coordenadores.id,
        or_(Ctrl_contrato.cntNome == salobo, Ctrl_contrato.cntNome == sossego),
        Ctrl_orcamentos.orcstatus == 'pendente'
        ).all()
    orcamento_json = []
    colunas = ('Nome','Descrição','Codigo','idchamado','idcontrato','id','dataEntrada','contrato','Coordenador','empresa')
    Tupple_to_json(orcamento_obj,orcamento_json,colunas)

    return gera_response(200, orcamento_json)




@orcamento.route('/read/orcamentos/bmsa/aguardando', methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
@jwt_required()
def Orcamento_filtro_bmsa_aguardando():
    salobo = 'Industrial Salobo'
    sossego = 'Industrial Sossego'
    orcamento_obj = db.session.query(
        Ctrl_orcamentos.orcnome, Ctrl_orcamentos.orcdescricao, Ctrl_orcamentos.orccodigo, Ctrl_chamados.id, Ctrl_contrato.id,Ctrl_orcamentos.id,
        Ctrl_chamados.chmEntrada, Ctrl_contrato.cntNome, Ctrl_coordenadores.codNome, Ctrl_coordenadores.codEmpresa
        ).filter(
        Ctrl_orcamentos.idchamado == Ctrl_chamados.id,
        Ctrl_chamados.idcnt == Ctrl_contrato.id,
        Ctrl_chamados.idCoordenador == Ctrl_coordenadores.id,
        or_(Ctrl_contrato.cntNome == salobo, Ctrl_contrato.cntNome == sossego),
        Ctrl_orcamentos.orcstatus == 'aguardando'
        ).all()
    orcamento_json = []
    colunas = ('Nome','Descrição','Codigo','idchamado','idcontrato','id','dataEntrada','contrato','Coordenador','empresa')
    Tupple_to_json(orcamento_obj,orcamento_json,colunas)

    return gera_response(200, orcamento_json)




@orcamento.route('/read/orcamentos/bmsa/liberado', methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
@jwt_required()
def Orcamento_filtro_bmsa_liberado():
    salobo = 'Industrial Salobo'
    sossego = 'Industrial Sossego'
    orcamento_obj = db.session.query(
        Ctrl_orcamentos.orcnome, Ctrl_orcamentos.orcdescricao, Ctrl_orcamentos.orccodigo, Ctrl_chamados.id, Ctrl_contrato.id,Ctrl_orcamentos.id,
        Ctrl_chamados.chmEntrada, Ctrl_contrato.cntNome, Ctrl_coordenadores.codNome, Ctrl_coordenadores.codEmpresa
        ).filter(
        Ctrl_orcamentos.idchamado == Ctrl_chamados.id,
        Ctrl_chamados.idcnt == Ctrl_contrato.id,
        Ctrl_chamados.idCoordenador == Ctrl_coordenadores.id,
        or_(Ctrl_contrato.cntNome == salobo, Ctrl_contrato.cntNome == sossego),
        Ctrl_orcamentos.orcstatus == 'liberado'
        ).all()
    orcamento_json = []
    colunas = ('Nome','Descrição','Codigo','idchamado','idcontrato','id','dataEntrada','contrato','Coordenador','empresa')
    Tupple_to_json(orcamento_obj,orcamento_json,colunas)

    return gera_response(200, orcamento_json)




@orcamento.route('/read/orcamentos/bmsa/cancelado', methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
@jwt_required()
def Orcamento_filtro_bmsa_cancelado():
    salobo = 'Industrial Salobo'
    sossego = 'Industrial Sossego'
    orcamento_obj = db.session.query(
        Ctrl_orcamentos.orcnome, Ctrl_orcamentos.orcdescricao, Ctrl_orcamentos.orccodigo, Ctrl_chamados.id, Ctrl_contrato.id,Ctrl_orcamentos.id,
        Ctrl_chamados.chmEntrada, Ctrl_contrato.cntNome, Ctrl_coordenadores.codNome, Ctrl_coordenadores.codEmpresa
        ).filter(
        Ctrl_orcamentos.idchamado == Ctrl_chamados.id,
        Ctrl_chamados.idcnt == Ctrl_contrato.id,
        Ctrl_chamados.idCoordenador == Ctrl_coordenadores.id,
        or_(Ctrl_contrato.cntNome == salobo, Ctrl_contrato.cntNome == sossego),
        Ctrl_orcamentos.orcstatus == 'cancelado'
        ).all()
    orcamento_json = []
    colunas = ('Nome','Descrição','Codigo','idchamado','idcontrato','id','dataEntrada','contrato','Coordenador','empresa')
    Tupple_to_json(orcamento_obj,orcamento_json,colunas)

    return gera_response(200, orcamento_json)
#
#
#
# todos os filtros do sudeste
#
#
#
@orcamento.route('/read/orcamentos/sudeste/pendente', methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
@jwt_required()
def Orcamento_filtro_sudeste_pendente():

    orcamento_obj = db.session.query(
        Ctrl_orcamentos.orcnome, Ctrl_orcamentos.orcdescricao, Ctrl_orcamentos.orccodigo, Ctrl_chamados.id, Ctrl_contrato.id,Ctrl_orcamentos.id,
        Ctrl_chamados.chmEntrada, Ctrl_contrato.cntNome, Ctrl_coordenadores.codNome, Ctrl_coordenadores.codEmpresa
        ).filter(
        Ctrl_orcamentos.idchamado == Ctrl_chamados.id,
        Ctrl_chamados.idcnt == Ctrl_contrato.id,
        Ctrl_chamados.idCoordenador == Ctrl_coordenadores.id,
        Ctrl_contrato.cntNome == 'Engenharia Industrial(sudeste)',
        Ctrl_orcamentos.orcstatus == 'pendente'
        ).all()
    orcamento_json = []
    colunas = ('Nome','Descrição','Codigo','idchamado','idcontrato','id','dataEntrada','contrato','Coordenador','empresa')
    Tupple_to_json(orcamento_obj,orcamento_json,colunas)

    return gera_response(200, orcamento_json)




@orcamento.route('/read/orcamentos/sudeste/aguardando', methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
@jwt_required()
def Orcamento_filtro_sudeste_aguardando():

    orcamento_obj = db.session.query(
        Ctrl_orcamentos.orcnome, Ctrl_orcamentos.orcdescricao, Ctrl_orcamentos.orccodigo, Ctrl_chamados.id, Ctrl_contrato.id,Ctrl_orcamentos.id,
        Ctrl_chamados.chmEntrada, Ctrl_contrato.cntNome, Ctrl_coordenadores.codNome, Ctrl_coordenadores.codEmpresa
        ).filter(
        Ctrl_orcamentos.idchamado == Ctrl_chamados.id,
        Ctrl_chamados.idcnt == Ctrl_contrato.id,
        Ctrl_chamados.idCoordenador == Ctrl_coordenadores.id,
        Ctrl_contrato.cntNome == 'Engenharia Industrial(sudeste)',
        Ctrl_orcamentos.orcstatus == 'aguardando'
        ).all()
    orcamento_json = []
    colunas = ('Nome','Descrição','Codigo','idchamado','idcontrato','id','dataEntrada','contrato','Coordenador','empresa')
    Tupple_to_json(orcamento_obj,orcamento_json,colunas)

    return gera_response(200, orcamento_json)




@orcamento.route('/read/orcamentos/sudeste/liberado', methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
@jwt_required()
def Orcamento_filtro_sudeste_liberado():

    orcamento_obj = db.session.query(
        Ctrl_orcamentos.orcnome, Ctrl_orcamentos.orcdescricao, Ctrl_orcamentos.orccodigo, Ctrl_chamados.id, Ctrl_contrato.id,Ctrl_orcamentos.id,
        Ctrl_chamados.chmEntrada, Ctrl_contrato.cntNome, Ctrl_coordenadores.codNome, Ctrl_coordenadores.codEmpresa
        ).filter(
        Ctrl_orcamentos.idchamado == Ctrl_chamados.id,
        Ctrl_chamados.idcnt == Ctrl_contrato.id,
        Ctrl_chamados.idCoordenador == Ctrl_coordenadores.id,
        Ctrl_contrato.cntNome == 'Engenharia Industrial(sudeste)',
        Ctrl_orcamentos.orcstatus == 'liberado'
        ).all()
    orcamento_json = []
    colunas = ('Nome','Descrição','Codigo','idchamado','idcontrato','id','dataEntrada','contrato','Coordenador','empresa')
    Tupple_to_json(orcamento_obj,orcamento_json,colunas)

    return gera_response(200, orcamento_json)




@orcamento.route('/read/orcamentos/sudeste/cancelado', methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
@jwt_required()
def Orcamento_filtro_sudeste_cancelado():

    orcamento_obj = db.session.query(
        Ctrl_orcamentos.orcnome, Ctrl_orcamentos.orcdescricao, Ctrl_orcamentos.orccodigo, Ctrl_chamados.id, Ctrl_contrato.id,Ctrl_orcamentos.id,
        Ctrl_chamados.chmEntrada, Ctrl_contrato.cntNome, Ctrl_coordenadores.codNome, Ctrl_coordenadores.codEmpresa
        ).filter(
        Ctrl_orcamentos.idchamado == Ctrl_chamados.id,
        Ctrl_chamados.idcnt == Ctrl_contrato.id,
        Ctrl_chamados.idCoordenador == Ctrl_coordenadores.id,
        Ctrl_contrato.cntNome == 'Engenharia Industrial(sudeste)',
        Ctrl_orcamentos.orcstatus == 'cancelado'
        ).all()
    orcamento_json = []
    colunas = ('Nome','Descrição','Codigo','idchamado','idcontrato','id','dataEntrada','contrato','Coordenador','empresa')
    Tupple_to_json(orcamento_obj,orcamento_json,colunas)

    return gera_response(200, orcamento_json)





