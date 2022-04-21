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




auth = Blueprint('auth', __name__)
chave_registro = "!@keyprojetacs"


@auth.route('/register', methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def register():
    try:
        email = request.json.get('email', None)
        password = request.json.get('password', None)
        key = request.json.get('key', None)
        
        if not email:
            return 'Missing email', 400
        if not password:
            return 'Missing password', 400
        if not key:
            return 'Missing key', 400
        
        if key != chave_registro:
            return 'wrong key', 400
        
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        user = User(email=email, hash=hashed)
        db.session.add(user)
        db.session.commit()

        access_token = create_access_token(identity={"email": email})
        return {"access_token": access_token}, 200
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
        email = request.json.get('email', None)
        password = request.json.get('password', None)
        
        if not email:
            return 'Missing email', 400
        if not password:
            return 'Missing password', 400
        
        user = User.query.filter_by(email=email).first()
        if not user:
            return 'User Not Found!', 404
        

        if bcrypt.checkpw(password.encode('utf-8'), user.hash):
            access_token = create_access_token(identity={"email": email})
            return {"access_token": access_token}, 200
        else:
            return 'Invalid Login Info!', 400
    except AttributeError:
        return 'Provide an Email and Password in JSON format in the request body', 400

# protected test route
@auth.route('/test', methods=['GET'])
@jwt_required()
def test():
    user = get_jwt_identity()
    email = user['email']
    return f'Welcome to the protected route {email}!', 200