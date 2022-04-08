from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import (JWTManager)

app = Flask(__name__, template_folder='.')
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['JWT_SECRET_KEY'] = '!0projetacsVision'
jwt = JWTManager(app)


from databaseApi.clientes.views import clientes
app.register_blueprint(clientes)
from databaseApi.auth.views import auth
app.register_blueprint(auth)
from databaseApi.escopo.views import escopo
app.register_blueprint(escopo)

