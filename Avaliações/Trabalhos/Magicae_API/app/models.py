from app import db

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