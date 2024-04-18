from app import db 

class Membros(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    idade = db.Column(db.Integer)
    nascimento = db.Column(db.Date)
    sexo = db.Column(db.String(20))
    cpf = db.Column(db.String(20), unique=True)
    rg = db.Column(db.String(15),unique=True)
    e_civil = db.Column(db.String(100))
    cidade_estado = db.Column(db.String(100))

    def __init__(self,nome,idade,nascimento,sexo,cpf,rg,e_civil,cidade_estado):
        self.nome = nome
        self.idade = idade
        self.nascimento = nascimento
        self.sexo = sexo 
        self.cpf = cpf
        self.rg = rg
        self.e_civil = e_civil
        self.cidade_estado = cidade_estado

class Atas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer)
    tipo = db.Column(db.String(100))
    presidente_secao = db.Column(db.String(30))
    data = db.Column(db.Date)
    membros_presentes = db.Column(db.Integer)
    texto = db.Column(db.String(255))

    def __init__(self, numero, tipo, presidente_secao, data, membros_presentes,texto):
        self.numero = numero
        self.tipo = tipo
        self.presidente_secao = presidente_secao
        self.data = data
        self.membros_presentes = membros_presentes
        self.texto = texto

class Lideranca(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    presidente = db.Column(db.String(100))
    vice_presidente = db.Column(db.String(100))
    secretario = db.Column(db.String(100))
    vice_secretario = db.Column(db.String(100))
    tesoureiro = db.Column(db.String(100))
    vice_tesoureiro = db.Column(db.String(100))
    membros_id = db.Column(db.Integer, db.ForeignKey('membros.id'))     

class Contato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    mensagem = db.Column(db.String(255))

    def __init__(self, nome, email, mensagem):
        self.nome = nome
        self.email = email
        self.mensagem = mensagem
