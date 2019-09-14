from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Usuarios(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150))
    email = db.Column(db.String(150))
    email = db.Column(db.String(150))
    ativo = db.Column(db.Boolean)

    def __init__(self, nome, email, ativo=True):
        self.nome = nome
        self.email = email
        self.ativo = ativo
