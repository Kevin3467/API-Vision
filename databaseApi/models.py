from databaseApi import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.Text, unique=True, nullable=False)
    hash = db.Column(db.Text, nullable=False)


class Ctrl_contrato(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True )
    cntCodigo = db.Column(db.String(80), nullable = False )
    cntNome = db.Column(db.String(80), nullable = False )
    cntValor = db.Column(db.Integer, nullable = False)
    cntGestor = db.Column(db.String(80), nullable = False)
    cntDataInicio = db.Column(db.String(14), nullable = False)
    cntDataFim = db.Column(db.String(14), nullable = False)

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




class Ctrl_qqp(db.Model):
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




class Ctrl_clientes(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True )
    clnNome = db.Column(db.String(80), nullable = False )
    clnEmpresa = db.Column(db.String(80), nullable = False )
    clnTelefone = db.Column(db.String(80))
    clnEmail = db.Column(db.String(255))
    
    def to_json(self):
        return {
        'id': self.id,
        'nome': self.clnNome,
        'empresa': self.clnEmpresa,
        'telefone': self.clnTelefone,
        'email': self.clnEmail
        }




class Ctrl_colaboradores(db.Model):
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
    id = db.Column(db.Integer, primary_key = True, autoincrement=True )
    escEscopo = db.Column(db.String(3000), nullable = False)
    escForaDeEscopo = db.Column(db.String(3000), nullable = False)
    escObjetivo = db.Column(db.String(3000), nullable = False)
    escSituacaoAtual = db.Column(db.String(2000), nullable = False)
    escPremissas = db.Column(db.String(2000), nullable = False)
    escFornecimentos = db.Column(db.String(2000), nullable = False)

    def to_json(self):
        return {
        'id': self.id,
        'escEscopo': self.escEscopo,
        'escForaDeEscopo': self.escForaDeEscopo,
        'escSituacaoAtual': self.escSituacaoAtual,
        'escPremissas': self.escPremissas,
        'escFornecimentos': self.escFornecimentos
        }


class Ctrl_chamados(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True )
    idesc = Ctrl_escopo.id
    idcnt = Ctrl_contrato.id
    chmSolicitacao = db.Column(db.String(80), nullable = False)
    chmTitulo = db.Column(db.String(255), nullable = False)
    chmDescricao = db.Column(db.String(255), nullable = False)
    idClientes = Ctrl_clientes.id
    idCoordenador = Ctrl_clientes.id
    chmVisita = db.Column(db.String(14))
    chmEmissão = db.Column(db.String(14))
    chmAprovação = db.Column(db.String(14))
    chmEntrega = db.Column(db.String(14))
    chmArquivamento = db.Column(db.String(14) )

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
        }