from flask import request, jsonify
from flask_jwt_extended import jwt_required
from app import db
from app.models import Casas
from datetime import datetime

@jwt_required()
def listar_casas():
    casas = Casas.query.all()
    return jsonify([{
        'id': casa.id,
        'nome': casa.nome,
        'simbolo': casa.simbolo,
    } for casa in casas])