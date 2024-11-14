from flask import request, jsonify
from app import db
from app.models import Disciplinas
from datetime import datetime

def listar_disciplinas():
    disciplinas = Disciplinas.query.all()
    return jsonify([{
        'id': disciplina.id,
        'nome': disciplina.nome,
        'descricao': disciplina.descricao,
    } for disciplina in disciplinas])

def adicionar_disciplina():
    data = request.get_json()
    novo_disciplina = Disciplinas(
        nome=data['nome'],
        descricao=data['descricao']
    )
    db.session.add(novo_disciplina)
    db.session.commit()
    return jsonify({'message': 'disciplina adicionado com sucesso!'})

def editar_disciplina(disciplina_id):
    data = request.get_json()
    disciplina = Disciplinas.query.get(disciplina_id)
    if not disciplina:
        return jsonify({'message': 'disciplina não encontrado'}), 404
    
    disciplina.nome = data['nome']
    disciplina.descricao = data['descricao']
    db.session.commit()
    return jsonify({'message': 'disciplina editado com sucesso!'})

def excluir_disciplina(disciplina_id):
    disciplina = Disciplinas.query.get(disciplina_id)
    if not disciplina:
        return jsonify({'message': 'disciplina não encontrado'}), 404

    db.session.delete(disciplina)
    db.session.commit()
    return jsonify({'message': 'disciplina excluído com sucesso!'})
