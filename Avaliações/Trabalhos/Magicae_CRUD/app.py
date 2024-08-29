from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector
from datetime import datetime
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB

app = Flask(__name__)
app.secret_key = 'your_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin):
    def __init__(self, id, username, user_type):
        self.id = id
        self.username = username
        self.user_type = user_type

@login_manager.user_loader
def load_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM usuarios WHERE id = %s', (user_id,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    if user:
        return User(user['id'], user['username'], user['user_type'])
    return None

def get_db_connection():
    return mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB
    )

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM usuarios WHERE username = %s', (username,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        if user and check_password_hash(user['password'], password):
            user_obj = User(user['id'], user['username'], user['user_type'])
            login_user(user_obj)
            return redirect(url_for('index'))
        flash('Invalid username or password')
    return render_template('login.html')

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_type = request.form['user_type']
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO usuarios (username, password, user_type) VALUES (%s, %s, %s)',
                       (username, hashed_password, user_type))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('login'))
    return render_template('cadastrar.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/')
@login_required
def index():
    return render_template('index.html', user_type=current_user.user_type)

@app.route('/professores')
@login_required
def professores():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    query = '''
    SELECT p.id, p.nome, p.data_nascimento, p.patrono, 
           c.nome AS casa_nome, 
           f.nome AS feitico_favorito, 
           d.nome AS disciplina_nome
    FROM professores p
    LEFT JOIN casas c ON p.casa_id = c.id
    LEFT JOIN feiticos f ON p.feitico_favorito_id = f.id
    LEFT JOIN disciplinas d ON p.disciplina_id = d.id
    '''
    cursor.execute(query)
    professores = cursor.fetchall()
    
    today = datetime.now().date()
    for professor in professores:
        if professor['data_nascimento']:
            birth_date = professor['data_nascimento']
            age = today.year - birth_date.year
            if today < birth_date.replace(year=today.year):
                age -= 1
            professor['idade'] = age
        else:
            professor['idade'] = 'Desconhecida'
    cursor.close()
    conn.close()
    
    return render_template('professores.html', professores=professores, user_type=current_user.user_type)

@app.route('/adicionar_professor', methods=('GET', 'POST'))
@login_required
def adicionar_professor():
    if current_user.user_type != 'professor':
        return "Acesso negado"
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST':
        nome = request.form['nome']
        data_nascimento = request.form['data_nascimento']
        casa_id = request.form['casa_id']
        feitico_favorito_id = request.form['feitico_favorito_id']
        disciplina_id = request.form['disciplina_id']
        patrono = request.form['patrono']
        
        cursor.execute('INSERT INTO professores (nome, data_nascimento, casa_id, feitico_favorito_id, disciplina_id, patrono) VALUES (%s, %s, %s, %s, %s, %s)',
                       (nome, data_nascimento, casa_id, feitico_favorito_id, disciplina_id, patrono))
        conn.commit()
        return redirect(url_for('professores'))
    else:
        # Consultar as tabelas necessárias
        cursor.execute('SELECT * FROM casas')
        casas = cursor.fetchall()
        cursor.execute('SELECT * FROM feiticos')
        feiticos = cursor.fetchall()
        cursor.execute('SELECT * FROM disciplinas')
        disciplinas = cursor.fetchall()

        cursor.close()
        conn.close()

        return render_template('adicionar_professor.html', casas=casas, feiticos=feiticos, disciplinas=disciplinas)


@app.route('/editar_professor/<int:id>', methods=('GET', 'POST'))
@login_required
def editar_professor(id):
    if current_user.user_type != 'professor':
        return "Acesso negado"
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST':
        nome = request.form['nome']
        data_nascimento = request.form['data_nascimento']
        casa_id = request.form['casa_id']
        feitico_favorito_id = request.form['feitico_favorito_id']
        disciplina_id = request.form['disciplina_id']
        patrono = request.form['patrono']
        
        cursor.execute('UPDATE professores SET nome = %s, data_nascimento = %s, casa_id = %s, feitico_favorito_id = %s, disciplina_id = %s, patrono = %s WHERE id = %s',
                       (nome, data_nascimento, casa_id, feitico_favorito_id, disciplina_id, patrono, id))
        conn.commit()
        return redirect(url_for('professores'))
    else:
        cursor.execute('SELECT * FROM casas')
        casas = cursor.fetchall()
        cursor.execute('SELECT * FROM feiticos')
        feiticos = cursor.fetchall()
        cursor.execute('SELECT * FROM disciplinas')
        disciplinas = cursor.fetchall()

        cursor.execute('SELECT * FROM professores WHERE id = %s', (id,))
        professor = cursor.fetchone()

        cursor.close()
        conn.close()

        return render_template('editar_professor.html', professor=professor, casas=casas, feiticos=feiticos, disciplinas=disciplinas)


@app.route('/excluir_professor/<int:id>', methods=('POST',))
@login_required
def excluir_professor(id):
    if current_user.user_type != 'professor':
        return "Acesso negado"
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM professores WHERE id = %s', (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('professores'))

@app.route('/alunos')
@login_required
def alunos():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    query = '''
    SELECT p.id, p.nome, p.data_nascimento, p.patrono, 
           c.nome AS casa_nome, 
           f.nome AS feitico_favorito, 
           d.nome AS disciplina_nome
    FROM alunos p
    LEFT JOIN casas c ON p.casa_id = c.id
    LEFT JOIN feiticos f ON p.feitico_favorito_id = f.id
    LEFT JOIN disciplinas d ON p.disciplina_id = d.id
    '''
    cursor.execute(query)
    alunos = cursor.fetchall()
    
    today = datetime.now().date()
    for aluno in alunos:
        if aluno['data_nascimento']:
            birth_date = aluno['data_nascimento']
            idade = today.year - birth_date.year
            if today < birth_date.replace(year=today.year):
                idade -= 1
            aluno['idade'] = idade
        else:
            aluno['idade'] = 'Desconhecida'
    cursor.close()
    conn.close()
    
    return render_template('alunos.html', alunos=alunos, user_type=current_user.user_type)

@app.route('/adicionar_aluno', methods=('GET', 'POST'))
@login_required
def adicionar_aluno():
    if current_user.user_type != 'professor':
        return "Acesso negado"
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST':
        nome = request.form['nome']
        data_nascimento = request.form['data_nascimento']
        casa_id = request.form['casa_id']
        feitico_favorito_id = request.form['feitico_favorito_id']
        disciplina_id = request.form['disciplina_id']
        patrono = request.form['patrono']
        
        cursor.execute('INSERT INTO alunos (nome, data_nascimento, casa_id, feitico_favorito_id, disciplina_id, patrono) VALUES (%s, %s, %s, %s, %s, %s)',
                       (nome, data_nascimento, casa_id, feitico_favorito_id, disciplina_id, patrono))
        conn.commit()
        return redirect(url_for('alunos'))
    else:
        cursor.execute('SELECT * FROM casas')
        casas = cursor.fetchall()
        cursor.execute('SELECT * FROM feiticos')
        feiticos = cursor.fetchall()
        cursor.execute('SELECT * FROM disciplinas')
        disciplinas = cursor.fetchall()

        cursor.close()
        conn.close()

        return render_template('adicionar_aluno.html', casas=casas, feiticos=feiticos, disciplinas=disciplinas)

@app.route('/editar_aluno/<int:id>', methods=('GET', 'POST'))
@login_required
def editar_aluno(id):
    if current_user.user_type != 'professor':
        return "Acesso negado"
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST':
        nome = request.form['nome']
        data_nascimento = request.form['data_nascimento']
        casa_id = request.form['casa_id']
        feitico_favorito_id = request.form['feitico_favorito_id']
        disciplina_id = request.form['disciplina_id']
        patrono = request.form['patrono']
        
        cursor.execute('UPDATE alunos SET nome = %s, data_nascimento = %s, casa_id = %s, feitico_favorito_id = %s, disciplina_id = %s, patrono = %s WHERE id = %s',
                       (nome, data_nascimento, casa_id, feitico_favorito_id, disciplina_id, patrono, id))
        conn.commit()
        return redirect(url_for('alunos'))
    else:
        cursor.execute('SELECT * FROM casas')
        casas = cursor.fetchall()
        cursor.execute('SELECT * FROM feiticos')
        feiticos = cursor.fetchall()
        cursor.execute('SELECT * FROM disciplinas')
        disciplinas = cursor.fetchall()

        cursor.execute('SELECT * FROM alunos WHERE id = %s', (id,))
        aluno = cursor.fetchone()

        cursor.close()
        conn.close()

        return render_template('editar_aluno.html', aluno=aluno, casas=casas, feiticos=feiticos, disciplinas=disciplinas)

@app.route('/excluir_aluno/<int:id>', methods=('POST',))
@login_required
def excluir_aluno(id):
    if current_user.user_type != 'professor':
        return "Acesso negado"
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM alunos WHERE id = %s', (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('alunos'))


@app.route('/feiticos')
@login_required
def feiticos():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    query = '''
    SELECT id, nome, descricao FROM feiticos
    '''
    cursor.execute(query)
    feiticos = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return render_template('feiticos.html', feiticos=feiticos, user_type=current_user.user_type)


@app.route('/adicionar_feitico', methods=('GET', 'POST'))
@login_required
def adicionar_feitico():
    if current_user.user_type != 'professor':
        return "Acesso negado"    
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        
        cursor.execute('INSERT INTO feiticos (nome, descricao) VALUES (%s, %s)',
                       (nome, descricao))
        conn.commit()
        return redirect(url_for('feiticos'))
    else:
        cursor.execute('SELECT * FROM feiticos')
        feiticos = cursor.fetchall()

        cursor.close()
        conn.close()

        return render_template('adicionar_feitico.html',feiticos=feiticos)

@app.route('/editar_feitico/<int:id>', methods=('GET', 'POST'))
@login_required
def editar_feitico(id):
    if current_user.user_type != 'professor':
        return "Acesso negado"
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        
        cursor.execute('UPDATE feiticos SET nome = %s, descricao = %s WHERE id = %s',
                       (nome, descricao, id))
        conn.commit()
        return redirect(url_for('feiticos'))
    else:
        cursor.execute('SELECT * FROM feiticos')
        feiticos = cursor.fetchall()

        cursor.execute('SELECT * FROM feiticos WHERE id = %s', (id,))
        feitico = cursor.fetchone()

        cursor.close()
        conn.close()

        return render_template('editar_feitico.html', feiticos=feiticos, feitico=feitico)

@app.route('/excluir_feitico/<int:id>', methods=('POST',))
@login_required
def excluir_feitico(id):
    if current_user.user_type != 'professor':
        return "Acesso negado"
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute('SELECT COUNT(*) AS total FROM professores WHERE feitico_favorito_id = %s', (id,))
    total_professores = cursor.fetchone()
    
    cursor.execute('SELECT COUNT(*) AS total FROM alunos WHERE feitico_favorito_id = %s', (id,))
    total_alunos = cursor.fetchone()
    
    if total_professores['total'] > 0 or total_alunos['total'] > 0:
        cursor.close()
        conn.close()
        return "Não é possível excluir um feitiço com professores ou alunos vinculados."
    
    cursor.execute('DELETE FROM feiticos WHERE id = %s', (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('feiticos'))



@app.route('/disciplinas')
@login_required
def disciplinas():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    query = '''
    SELECT id, nome, descricao FROM disciplinas
    '''
    cursor.execute(query)
    disciplinas = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return render_template('disciplinas.html', disciplinas=disciplinas, user_type=current_user.user_type)


@app.route('/adicionar_disciplina', methods=('GET', 'POST'))
@login_required
def adicionar_disciplina():
    if current_user.user_type != 'professor':
        return "Acesso negado"    
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        
        cursor.execute('INSERT INTO disciplinas (nome, descricao) VALUES (%s, %s)',
                       (nome, descricao))
        conn.commit()
        return redirect(url_for('disciplinas'))
    else:
        cursor.execute('SELECT * FROM disciplinas')
        disciplinas = cursor.fetchall()

        cursor.close()
        conn.close()

        return render_template('adicionar_disciplina.html',disciplinas=disciplinas)

@app.route('/editar_disciplina/<int:id>', methods=('GET', 'POST'))
@login_required
def editar_disciplina(id):
    if current_user.user_type != 'professor':
        return "Acesso negado"
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        
        cursor.execute('UPDATE disciplinas SET nome = %s, descricao = %s WHERE id = %s',
                       (nome, descricao, id))
        conn.commit()
        return redirect(url_for('disciplinas'))
    else:
        cursor.execute('SELECT * FROM disciplinas')
        disciplinas = cursor.fetchall()

        cursor.execute('SELECT * FROM disciplinas WHERE id = %s', (id,))
        disciplina = cursor.fetchone()

        cursor.close()
        conn.close()

        return render_template('editar_disciplina.html', disciplinas=disciplinas, disciplina=disciplina)

@app.route('/excluir_disciplina/<int:id>', methods=('POST',))
@login_required
def excluir_disciplina(id):
    if current_user.user_type != 'professor':
        return "Acesso negado"
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute('SELECT COUNT(*) AS total FROM professores WHERE disciplina_id = %s', (id,))
    total_professores = cursor.fetchone()
    
    cursor.execute('SELECT COUNT(*) AS total FROM alunos WHERE disciplina_id = %s', (id,))
    total_alunos = cursor.fetchone()
    
    if total_professores['total'] > 0 or total_alunos['total'] > 0:
        cursor.close()
        conn.close()
        return "Não é possível excluir uma disciplina com professores ou alunos vinculados."
    
    cursor.execute('DELETE FROM disciplinas WHERE id = %s', (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('disciplinas'))



if __name__ == '__main__':
    app.run(debug=True)
