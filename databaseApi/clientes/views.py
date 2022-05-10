from flask import Response, request, Blueprint
import json
from databaseApi import clientes, db
from databaseApi.main import gera_response
from databaseApi.models import Ctrl_clientes
from flask_jwt_extended import jwt_required
 
clientes = Blueprint('clientes', __name__)




# lista todos os clientes na tabela
@clientes.route('/read/clientes', methods=['GET'])
@jwt_required()
def Clientes():
    
    clientes_obj = Ctrl_clientes.query.all()
    clientes_json = [cliente.to_json() for cliente in clientes_obj]
    

    return gera_response(200, clientes_json)




# filtra clientes por ID
@clientes.route('/cliente/<id>', methods=['GET'])
@jwt_required()
def Cliente(id):

    cliente_obj = Ctrl_clientes.query.filter_by(id=id).first()
    cliente_json = cliente_obj.to_json()


    return gera_response(200, cliente_json)


# create clientes
@clientes.route('/create/cliente', methods=['POST'])
@jwt_required()
def CriaCliente():

    body = request.get_json()
    try:
        newcliente = Ctrl_clientes(
            id=body["id"],
            clnNome=body["nome"],
            clnEmpresa= body["empresa"],
            clnTelefone= body["telefone"],
            clnEmail= body["email"]
            )
        db.session.add(newcliente)
        db.session.commit()
        return gera_response(201, newcliente.to_json(), "Criado com sucesso")
    except Exception as e:
        print('Erro', e)
        return gera_response(400, {}, "Erro ao cadastrar")

    return Response()



# Atualizar cliente
@clientes.route("/cliente/<id>", methods=["PUT"])
@jwt_required()
def AtualizaCliente(id):

    cliente_objeto = Ctrl_clientes.query.filter_by(id=id).first()
    body = request.get_json()

    try:
        if('nome' in body):
            cliente_objeto.clnNome = body['nome']
        if('empresa' in body):
            cliente_objeto.clnEmpresa = body['empresa']
        if('telefone' in body):
            cliente_objeto.clnTelefone = body['telefone']
        if('email' in body):
            cliente_objeto.clnEmail = body['email']
            
        
        db.session.add(cliente_objeto)
        db.session.commit()
        return gera_response(200, cliente_objeto.to_json(), "Atualizado com sucesso")


    except Exception as e:
        print('Erro', e)
        return gera_response(400, {}, "Erro ao atualizar")



# Deletar
@clientes.route("/cliente/<id>", methods=["DELETE"])
@jwt_required()
def deleta_cliente(id):
    cliente_objeto = Ctrl_clientes.query.filter_by(id=id).first()

    try:
        db.session.delete(cliente_objeto)
        db.session.commit()
        return gera_response(200, cliente_objeto.to_json(), "Deletado com sucesso")
    except Exception as e:
        print('Erro', e)
        return gera_response(400, {}, "Erro ao deletar")


