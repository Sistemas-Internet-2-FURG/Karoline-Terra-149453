from flask import Blueprint, request, jsonify, redirect, url_for
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash
from app import db
from app.models import Usuarios  
from flask_jwt_extended import create_access_token
auth = Blueprint('auth', __name__)

@auth.route('/registro', methods=['POST'])
def registro():
    data = request.get_json()
    username = data['username']
    password = data['password']
    user_type = data['user_type']
    
    if Usuarios.query.filter_by(username=username).first():
        return jsonify({'message': 'Username already exists'}), 400

    hashed_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
    new_user = Usuarios(username=username, password_hash=hashed_password, user_type=user_type)

    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'Usuário registrado com sucesso'})

@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = Usuarios.query.filter_by(username=data['username']).first()
    if user and user.check_password(data['password']):
        login_user(user)
        access_token = create_access_token(identity=user.username)
        return jsonify({'message': 'Login realizado com sucesso!', 'access_token': access_token, 'user_type': user.user_type})
    return jsonify({'message': 'Credenciais inválidas'}), 401

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
