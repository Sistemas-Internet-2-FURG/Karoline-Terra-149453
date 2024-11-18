from flask import request, jsonify
from app import db
from app.models import Professores, Casas, Feiticos, Disciplinas
from datetime import datetime
from flask import jsonify, request
from flask_jwt_extended import jwt_required
from app.models import Professores, Casas, Feiticos, Disciplinas

@jwt_required()
def listar_professores():
    professores = Professores.query.all()
    resultado = []
    for professor in professores:
        casa = Casas.query.get(professor.casa_id)
        feitico = Feiticos.query.get(professor.feitico_favorito_id)
        disciplina = Disciplinas.query.get(professor.disciplina_id)

        resultado.append({
            'id': professor.id,
            'nome': professor.nome,
            'data_nascimento': professor.data_nascimento,
            'casa_nome': casa.nome if casa else 'Desconhecida',
            'feitico_favorito': feitico.nome if feitico else 'Desconhecido',
            'disciplina_nome': disciplina.nome if disciplina else 'Desconhecida',
            'patrono': professor.patrono
        })
    return jsonify(resultado)

@jwt_required()
def obter_professor(professor_id):
    professor = Professores.query.get(professor_id)
    if not professor:
        return jsonify({'message': 'Professor não encontrado'}), 404

    casa = Casas.query.get(professor.casa_id)
    feitico = Feiticos.query.get(professor.feitico_favorito_id)
    disciplina = Disciplinas.query.get(professor.disciplina_id)

    return jsonify({
        'id': professor.id,
        'nome': professor.nome,
        'data_nascimento': professor.data_nascimento,
        'casa_id': professor.casa_id,
        'casa_nome': casa.nome if casa else 'Desconhecida',
        'feitico_favorito_id': professor.feitico_favorito_id,
        'feitico_nome': feitico.nome if feitico else 'Desconhecido',
        'disciplina_id': professor.disciplina_id,
        'disciplina_nome': disciplina.nome if disciplina else 'Desconhecida',
        'patrono': professor.patrono
    })

@jwt_required()
def adicionar_professor():
    data = request.get_json()
    novo_professor = Professores(
        nome=data['nome'],
        data_nascimento=datetime.strptime(data['data_nascimento'], '%Y-%m-%d'),
        casa_id=data['casa_id'],
        feitico_favorito_id=data['feitico_favorito_id'],
        disciplina_id=data['disciplina_id'],
        patrono=data['patrono']
    )
    db.session.add(novo_professor)
    db.session.commit()
    return jsonify({'message': 'Professor adicionado com sucesso!'})

@jwt_required()
def editar_professor(professor_id):
    data = request.get_json()
    professor = Professores.query.get(professor_id)
    if not professor:
        return jsonify({'message': 'Professor não encontrado'}), 404
    
    professor.nome = data['nome']
    professor.data_nascimento = datetime.strptime(data['data_nascimento'], '%Y-%m-%d')
    professor.casa_id = data['casa_id']
    professor.feitico_favorito_id = data['feitico_favorito_id']
    professor.disciplina_id = data['disciplina_id']
    professor.patrono = data['patrono']
    db.session.commit()
    return jsonify({'message': 'Professor editado com sucesso!'})

@jwt_required()
def excluir_professor(professor_id):
    professor = Professores.query.get(professor_id)
    if not professor:
        return jsonify({'message': 'Professor não encontrado'}), 404

    db.session.delete(professor)
    db.session.commit()
    return jsonify({'message': 'Professor excluído com sucesso!'})
