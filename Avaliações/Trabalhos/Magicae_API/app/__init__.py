from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/magicae'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

try:
    from app import routes
    print("Importação de 'routes' bem-sucedida")
except ImportError as e:
    print(f"Erro ao importar 'routes': {e}")


