from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import (JWTManager)
from datetime import timedelta
from flask_migrate import Migrate

app = Flask(__name__, template_folder='.')
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://gicnsnsixmbhqs:2fa8fe4eb2f869061d5adecee9d2ba09dafdb5386ea6a52ac1fdb701c17227c3@ec2-52-70-186-184.compute-1.amazonaws.com:5432/dfnhlth983shho'
#db local para debug
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['JWT_SECRET_KEY'] = '!0projetacsVision'
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=2)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=2)
jwt = JWTManager(app)
migrate = Migrate(app,db)

from databaseApi.clientes.views import clientes
app.register_blueprint(clientes)
from databaseApi.auth.views import auth
app.register_blueprint(auth)
from databaseApi.escopo.views import escopo
app.register_blueprint(escopo)
from databaseApi.orcamento.views import orcamento
app.register_blueprint(orcamento)


