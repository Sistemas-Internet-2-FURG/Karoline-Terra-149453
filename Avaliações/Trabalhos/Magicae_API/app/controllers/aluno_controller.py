from flask import request, jsonify
from app import db
from app.models import Alunos, Casas, Feiticos, Disciplinas
from datetime import datetime

def listar_alunos():
    alunos = Alunos.query.all()
    resultado = []
    for aluno in alunos:
        casa = Casas.query.get(aluno.casa_id)
        feitico = Feiticos.query.get(aluno.feitico_favorito_id)
        disciplina = Disciplinas.query.get(aluno.disciplina_id)
        
        resultado.append({
            'id': aluno.id,
            'nome': aluno.nome,
            'data_nascimento': aluno.data_nascimento,
            'casa_nome': casa.nome if casa else 'Desconhecida',
            'feitico_favorito': feitico.nome if feitico else 'Desconhecido',
            'disciplina_nome': disciplina.nome if disciplina else 'Desconhecida',
            'patrono': aluno.patrono
        })
    return jsonify(resultado)

def obter_aluno(aluno_id):
    aluno = Alunos.query.get(aluno_id)
    if not aluno:
        return jsonify({'message': 'aluno não encontrado'}), 404

    casa = Casas.query.get(aluno.casa_id)
    feitico = Feiticos.query.get(aluno.feitico_favorito_id)
    disciplina = Disciplinas.query.get(aluno.disciplina_id)

    return jsonify({
        'id': aluno.id,
        'nome': aluno.nome,
        'data_nascimento': aluno.data_nascimento,
        'casa_id': aluno.casa_id,
        'casa_nome': casa.nome if casa else 'Desconhecida',
        'feitico_favorito_id': aluno.feitico_favorito_id,
        'feitico_nome': feitico.nome if feitico else 'Desconhecido',
        'disciplina_id': aluno.disciplina_id,
        'disciplina_nome': disciplina.nome if disciplina else 'Desconhecida',
        'patrono': aluno.patrono
    })

def adicionar_aluno():
    data = request.get_json()
    novo_aluno = Alunos(
        nome=data['nome'],
        data_nascimento=datetime.strptime(data['data_nascimento'], '%Y-%m-%d'),
        feitico_favorito_id=data['feitico_favorito_id'],
        patrono=data['patrono'],
        casa_id=data['casa_id'],
        disciplina_id=data['disciplina_id']
    )
    db.session.add(novo_aluno)
    db.session.commit()
    return jsonify({'message': 'aluno adicionado com sucesso!'})

def editar_aluno(aluno_id):
    data = request.get_json()
    aluno = Alunos.query.get(aluno_id)
    if not aluno:
        return jsonify({'message': 'aluno não encontrado'}), 404
    
    aluno.nome = data['nome']
    aluno.data_nascimento = datetime.strptime(data['data_nascimento'], '%Y-%m-%d')
    aluno.feitico_favorito_id = data['feitico_favorito_id']
    aluno.patrono = data['patrono']
    aluno.casa_id = data['casa_id']
    aluno.disciplina_id = data['disciplina_id']
    db.session.commit()
    return jsonify({'message': 'aluno editado com sucesso!'})

def excluir_aluno(aluno_id):
    aluno = Alunos.query.get(aluno_id)
    if not aluno:
        return jsonify({'message': 'aluno não encontrado'}), 404

    db.session.delete(aluno)
    db.session.commit()
    return jsonify({'message': 'aluno excluído com sucesso!'})
