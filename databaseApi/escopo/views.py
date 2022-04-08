from flask import request, Blueprint
import json
from databaseApi import db
from databaseApi.main import gera_response
from databaseApi.models import Ctrl_escopo
from flask_jwt_extended import jwt_required

escopo = Blueprint('escopo', __name__)


# lista todos os clientes na tabela
@escopo.route('/read/escopos', methods=['GET'])
@jwt_required()
def Escopos():

    escopo_obj = Ctrl_escopo.query.all()
    escopo_json = [escopo.to_json() for escopo in escopo_obj]


    return gera_response(200, "escopos", escopo_json)



# filtra clientes por ID
@escopo.route('/escopo/<id>', methods=['GET'])
@jwt_required()
def Escopo(id):

    escopo_obj = Ctrl_escopo.query.filter_by(id=id).first()
    escopo_json = escopo_obj.to_json()


    return gera_response(200, "escopo", escopo_json)





# create clientes
@escopo.route('/create/escopo', methods=['POST'])
@jwt_required()
def CriaEscopo():

    body = request.get_json()
    try:
        newescopo = Ctrl_escopo(
            escEscopo= body["escEscopo"],
            escObjetivo= body["escObjetivo"],
            escForaDeEscopo= body["escForaDeEscopo"],
            escSituacaoAtual= body["escSituacaoAtual"],
            escPremissas= body["escPremissas"],
            escFornecimentos= body["escFornecimentos"]
            )
        db.session.add(newescopo)
        db.session.commit()
        return gera_response(201, "escopo", newescopo.to_json(), "Criado com sucesso")
    except Exception as e:
        print('Erro', e)
        return gera_response(400, "escopo", {}, "Erro ao cadastrar")

    return Response()



# Atualizar cliente
@escopo.route("/escopo/<id>", methods=["PUT"])
@jwt_required()
def AtualizaEscopo(id):

    escopo_objeto = Ctrl_escopo.query.filter_by(id=id).first()
    body = request.get_json()

    try:
        if('escEscopo' in body):
            escopo_objeto.escEscopo = body['escEscopo']
        if('escObjetivo' in body):
            escopo_objeto.escObjetivo = body['escObjetivo']
        if('escForaDeEscopo' in body):
            escopo_objeto.escForaDeEscopo = body['escForaDeEscopo']
        if('escSituacaoAtual' in body):
            escopo_objeto.escSituacaoAtual = body['escSituacaoAtual']
        if('escPremissas' in body):
            escopo_objeto.escPremissas = body['escPremissas']
        if('escFornecimentos' in body):
            escopo_objeto.escFornecimentos = body['escFornecimentos']
            
        
        db.session.add(escopo_objeto)
        db.session.commit()
        return gera_response(200, "escopo", escopo_objeto.to_json(), "Atualizado com sucesso")


    except Exception as e:
        print('Erro', e)
        return gera_response(400, "escopo", {}, "Erro ao atualizar")


# Deletar
@escopo.route("/escopo/<id>", methods=["DELETE"])
@jwt_required()
def deleta_cliente(id):
    escopo_objeto = Ctrl_escopo.query.filter_by(id=id).first()

    try:
        db.session.delete(escopo_objeto)
        db.session.commit()
        return gera_response(200, "escopo", escopo_objeto.to_json(), "Deletado com sucesso")
    except Exception as e:
        print('Erro', e)
        return gera_response(400, "escopo", {}, "Erro ao deletar")
