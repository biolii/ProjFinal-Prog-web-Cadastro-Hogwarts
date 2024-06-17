from . import db
from werkzeug.security import generate_password_hash, check_password_hash

class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    casa = db.Column(db.String(50), nullable=False)
    ano = db.Column(db.Integer, nullable=False)
    especialidades = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Aluno {self.nome}>'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)