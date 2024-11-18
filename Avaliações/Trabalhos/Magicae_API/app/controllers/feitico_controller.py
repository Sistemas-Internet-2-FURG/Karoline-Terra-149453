from flask import request, jsonify
from flask_jwt_extended import jwt_required
from app import db
from app.models import Feiticos

@jwt_required()
def listar_feiticos():
    feiticos = Feiticos.query.all()
    return jsonify([{
        'id': feitico.id,
        'nome': feitico.nome,
        'descricao': feitico.descricao,
    } for feitico in feiticos])

@jwt_required()
def obter_feitico(feitico_id):
    feitico = Feiticos.query.get(feitico_id)
    if not feitico:
        return jsonify({'message': 'feitico não encontrada'}), 404

    return jsonify({
        'id': feitico.id,
        'nome': feitico.nome,
        'descricao': feitico.descricao
    })

@jwt_required()
def adicionar_feitico():
    data = request.get_json()
    novo_feitico = Feiticos(
        nome=data['nome'],
        descricao=data['descricao']
    )
    db.session.add(novo_feitico)
    db.session.commit()
    return jsonify({'message': 'feitico adicionado com sucesso!'})

@jwt_required()
def editar_feitico(feitico_id):
    data = request.get_json()
    feitico = Feiticos.query.get(feitico_id)
    if not feitico:
        return jsonify({'message': 'feitico não encontrado'}), 404
    
    feitico.nome = data['nome']
    feitico.descricao = data['descricao']
    db.session.commit()
    return jsonify({'message': 'feitico editado com sucesso!'})

@jwt_required()
def excluir_feitico(feitico_id):
    feitico = Feiticos.query.get(feitico_id)
    if not feitico:
        return jsonify({'message': 'feitico não encontrado'}), 404

    db.session.delete(feitico)
    db.session.commit()
    return jsonify({'message': 'feitico excluído com sucesso!'})
