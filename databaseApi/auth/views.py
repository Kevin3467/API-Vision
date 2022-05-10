from flask import Blueprint
from flask import Flask, request
import bcrypt
from flask_jwt_extended import (
    jwt_required,
    create_access_token,
    get_jwt_identity
)
from flask_cors import cross_origin
# Expetions for sqlaclemy
from sqlalchemy.exc import IntegrityError
#importing table class and the db conection
from databaseApi.models import User
from databaseApi import db
from databaseApi.main import gera_response




auth = Blueprint('auth', __name__)
chave_registro = "!@keyprojetacs"


@auth.route('/register', methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def register():
    try:
        username = request.json.get('username', None)
        password = request.json.get('password', None)
        user_type = request.json.get('user_type', None)
        cargo = request.json.get('cargo', None)

        key = request.json.get('key', None)
        
        if not username:
            return 'Missing email', 400
        if not user_type:
            return 'Missing email', 400
        if not cargo:
            return 'Missing email', 400
        if not password:
            return 'Missing password', 400
        if not key:
            return 'Missing key', 400
        
        if key != chave_registro:
            return 'wrong key', 400
        
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        user = User(username=username, hash=hashed,usertype=user_type,cargo=cargo)
        db.session.add(user)
        db.session.commit()

        
        return "Usuario criado com sucesso", 200
    except IntegrityError:
        # the rollback func reverts the changes made to the db ( so if an error happens after we commited changes they will be reverted )
        db.session.rollback()
        return 'User Already Exists', 400
    except AttributeError:
        return 'Provide an Email and Password in JSON format in the request body', 400


@auth.route('/login', methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def login():
    try:
        username = request.json.get('username', None)
        password = request.json.get('password', None)
        
        if not username:
            return 'Missing username', 400
        if not password:
            return 'Missing password', 400
        
        user = User.query.filter_by(username=username).first()
        if not user:
            return 'User Not Found!', 404
        

        if bcrypt.checkpw(password.encode('utf-8'), user.hash):
            access_token = create_access_token(identity={"username": username})
            return {"access_token": access_token}, 200
        else:
            return 'Invalid Login Info!', 400
    except AttributeError:
        return 'Provide an Email and Password in JSON format in the request body', 400




# protected test route
@auth.route('/user', methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
@jwt_required()
def CurrentUser():

    user_identity = get_jwt_identity()
    username = user_identity['username']
    user_obj = User.query.filter_by(username=username).first()
    user_json = user_obj.to_json()

    return gera_response(200, user_json)