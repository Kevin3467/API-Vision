from databaseApi import db




class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.Text, unique=True, nullable=False)
    hash = db.Column(db.LargeBinary, nullable=False)
    cargo = db.Column(db.Text, nullable=False)
    usertype = db.Column(db.Text, nullable=False)

    def to_json(self):
        return {
        'id': self.id,
        'username': self.username,
        'cargo': self.cargo,
        'usertype': self.usertype
        }

class Ctrl_contrato(db.Model):
    __tablename__ = 'contrato'


    id = db.Column(db.Integer, primary_key = True, autoincrement=True )
    cntCodigo = db.Column(db.Text, nullable = False )
    cntNome = db.Column(db.Text, nullable = False )
    cntValor = db.Column(db.Integer, nullable = False)
    cntGestor = db.Column(db.Text, nullable = False)
    cntDataInicio = db.Column(db.Text, nullable = False)
    cntDataFim = db.Column(db.Text, nullable = False)


    chamados = db.relationship('Ctrl_chamados')

    
    def to_json(self):
        return {
        'id': self.id,
        'cntCodigo': self.cntCodigo,
        'cntNome': self.cntNome,
        'cntValor': self.cntValor,
        'cntGestor': self.cntGestor,
        'cntDataInicio': self.cntDataInicio,
        'cntDataFim': self.cntDataFim
        }



class Ctrl_clientes(db.Model):
    __tablename__ = 'clientes'


    id = db.Column(db.Integer, primary_key = True, autoincrement=True )
    clnNome = db.Column(db.Text, nullable = False )
    clnEmpresa = db.Column(db.Text, nullable = False )
    clnTelefone = db.Column(db.Text)
    clnEmail = db.Column(db.Text)

    chamados = db.relationship('Ctrl_chamados')
    
    def to_json(self):
        return {
        'id': self.id,
        'nome': self.clnNome,
        'empresa': self.clnEmpresa,
        'telefone': self.clnTelefone,
        'email': self.clnEmail
        }


class Ctrl_orcamentos(db.Model):
    __tablename__ = 'orcamentos'


    id = db.Column(db.Integer, primary_key = True, autoincrement=True )
    orcnome = db.Column(db.Text, nullable = False )
    orcdescricao = db.Column(db.Text, nullable = False )
    orccodigo = db.Column(db.Text)
    orcstatus = db.Column(db.Text, nullable = False)
    idchamado = db.Column(db.Integer, db.ForeignKey('chamados.id'))

    
    def to_json(self):
        return {
        'id': self.id,
        'nome': self.orcnome,
        'descricao': self.orcdescricao,
        'codigo': self.orccodigo
        }



class Ctrl_coordenadores(db.Model):
    __tablename__ = 'coordenadores'


    id = db.Column(db.Integer, primary_key = True, autoincrement=True )
    codNome = db.Column(db.String(80), nullable = False )
    codEmpresa = db.Column(db.String(80), nullable = False )
    codTelefone = db.Column(db.String(80))
    codEmail = db.Column(db.String(255))

    
    chamados = db.relationship('Ctrl_chamados')
    
    def to_json(self):
        return {
        'id': self.id,
        'nome': self.clnNome,
        'empresa': self.clnEmpresa,
        'telefone': self.clnTelefone,
        'email': self.clnEmail
        }


class Ctrl_chamados(db.Model):
    __tablename__ = 'chamados'


    id = db.Column(db.Integer, primary_key = True, autoincrement=True )
    idcnt = db.Column(db.Integer, db.ForeignKey('contrato.id'))
    chmSolicitacao = db.Column(db.String(80), nullable = False)
    chmTitulo = db.Column(db.String(255), nullable = False)
    chmDescricao = db.Column(db.String(255), nullable = False)
    idClientes = db.Column(db.Integer, db.ForeignKey('clientes.id'))
    idCoordenador = db.Column(db.Integer, db.ForeignKey('coordenadores.id'))
    chmStatus = db.Column(db.Text, nullable = False)
    chmEntrada = db.Column(db.DateTime)
    chmVisita = db.Column(db.DateTime)
    chmEmissão = db.Column(db.DateTime)
    chmAprovação = db.Column(db.DateTime)
    chmEntrega = db.Column(db.DateTime)
    chmArquivamento = db.Column(db.DateTime)


    escopo = db.relationship('Ctrl_escopo')

    def to_json(self):
        return {
        'id': self.id,
        'idcnt': self.idcnt,
        'chmSolicitacao': self.chmSolicitacao,
        'chmTitulo': self.chmTitulo,
        'chmDescricao': self.chmDescricao,
        'idClientes': self.idClientes,
        'idCoordenador': self.idCoordenador,
        'chmVisita': self.chmVisita,
        'chmEmissão': self.chmEmissão,
        'chmAprovação': self.chmAprovação,
        'chmEntrega': self.chmEntrega,
        'chmArquivamento': self.chmArquivamento,
        'chmStatus': self.chmStatus,
        }




class Ctrl_colaboradores(db.Model):
    __tablename__ = 'colaboradores'

    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    clbNome = db.Column(db.String(80), nullable = False)
    clbCPFouCNPJ = db.Column(db.Integer, nullable = False)
    clbadmissão = db.Column(db.String(14), nullable = False)
    clbNascimento = db.Column(db.String(14), nullable = False)
    clbCargo = db.Column(db.String(80), nullable = False)
    clbDemissao = db.Column(db.String(14))

    def to_json(self):
        return {
        'id': self.id,
        'clbNome': self.clbNome,
        'clbCPFouCNPJ': self.clbCPFouCNPJ,
        'clbadmissão': self.clbadmissão,
        'clbNascimento': self.clbNascimento,
        'clbCargo': self.clbCargo,
        'clbDemissao': self.clbDemissao
        }




class Ctrl_escopo(db.Model):
    __tablename__ = 'escopo'


    id = db.Column(db.Integer, primary_key = True, autoincrement=True )
    idchamado = db.Column(db.Integer, db.ForeignKey('chamados.id'))
    escEscopo = db.Column(db.String(3000), nullable = False)
    escForaDeEscopo = db.Column(db.String(3000), nullable = False)
    escObjetivo = db.Column(db.String(3000), nullable = False)
    escSituacaoAtual = db.Column(db.String(2000), nullable = False)
    escPremissas = db.Column(db.String(2000), nullable = False)
    escFornecimentos = db.Column(db.String(2000), nullable = False)

    def to_json(self):
        return {
        'id': self.id,
        'idchamado': self.idchamado,
        'escEscopo': self.escEscopo,
        'escForaDeEscopo': self.escForaDeEscopo,
        'escSituacaoAtual': self.escSituacaoAtual,
        'escPremissas': self.escPremissas,
        'escFornecimentos': self.escFornecimentos
        }





class Ctrl_qqp(db.Model):
    __tablename__ = 'qqp'

    id = db.Column(db.Integer, primary_key = True, autoincrement=True )
    qqpCodigo = db.Column(db.String(80), nullable = False )
    idcnt = Ctrl_contrato.id
    qqpItem = db.Column(db.String(80), nullable = False)
    qqpDescricao = db.Column(db.String(80), nullable = False)
    qqpQuantidade = db.Column(db.Integer, nullable = False)
    qqpValor = db.Column(db.Integer, nullable = False)

    def to_json(self):
        return {
        'id': self.id,
        'qqpCodigo': self.qqpCodigo,
        'idcnt': self.idcnt,
        'qqpItem': self.qqpItem,
        'qqpDescricao': self.qqpDescricao,
        'qqpQuantidade': self.qqpQuantidade,
        'qqpValor': self.qqpValor
        }