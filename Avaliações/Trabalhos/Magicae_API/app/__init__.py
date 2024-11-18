from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/magicae'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'senhateste'
db = SQLAlchemy(app)

jwt = JWTManager(app)

app.secret_key = 'senhateste'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = ''

from app.models import Usuarios

@login_manager.user_loader
def load_user(user_id):
    return Usuarios.query.get(int(user_id))

from .import routes
from app.controllers.auth_controller import auth
app.register_blueprint(auth)




