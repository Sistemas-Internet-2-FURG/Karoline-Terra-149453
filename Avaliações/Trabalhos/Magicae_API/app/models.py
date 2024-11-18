from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Usuarios(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    user_type = db.Column(db.String(50), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'


class Professores(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    casa_id = db.Column(db.Integer, nullable=False)
    feitico_favorito_id = db.Column(db.Integer, nullable=False)
    disciplina_id = db.Column(db.Integer, nullable=False)
    patrono = db.Column(db.String(80), nullable=True)

    def __repr__(self):
        return f'<Professor {self.nome}>'

class Alunos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    casa_id = db.Column(db.Integer, nullable=False)
    feitico_favorito_id = db.Column(db.Integer, nullable=False)
    disciplina_id = db.Column(db.Integer, nullable=False)
    patrono = db.Column(db.String(80), nullable=True)

    def __repr__(self):
        return f'<Aluno {self.nome}>'
    
class Feiticos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(255), nullable=False)
    descricao = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Feitico {self.nome}>'


class Casas(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(255), nullable=False)
    simbolo = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<Casa {self.nome}>'

class Disciplinas(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(255), nullable=False)
    descricao = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Disciplina {self.nome}>'