from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Estudante(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150))
    idade = db.Column(db.Integer)

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def to_dict(self, columns=[]):
        if not columns:
            return {"id": self.id, "nome": self.nome, "idade": self.idade}
        else:
            return {col: getattr(self, col) for col in columns}
