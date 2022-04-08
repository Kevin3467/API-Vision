from databaseApi.models import db, Ctrl_contrato, Ctrl_qqp, Ctrl_clientes, Ctrl_chamados, Ctrl_colaboradores, Ctrl_escopo
from werkzeug.security import generate_password_hash

db.create_all()