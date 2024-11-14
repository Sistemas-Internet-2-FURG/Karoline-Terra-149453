from app import app
from flask import render_template, redirect, url_for
from app.controllers import professor_controller, feitico_controller, aluno_controller, disciplina_controller, casa_controller
from flask_login import login_required, logout_user

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/professores', methods=['GET'])
def professores():
    return render_template('professores.html')

@app.route('/editar_professor/<int:id>', methods=['GET'])
def editar_professor_render(id):
    return render_template('editar_professor.html')

@app.route('/adicionar_professor', methods=['GET'])
def adicionar_professor_render():
    return render_template('adicionar_professor.html')

@app.route('/feiticos', methods=['GET'])
def feiticos():
    return render_template('feiticos.html')

@app.route('/editar_feitico/<int:id>', methods=['GET'])
def editar_feitico_render(id):
    return render_template('editar_feitico.html')

@app.route('/adicionar_feitico', methods=['GET'])
def adicionar_feitico_render():
    return render_template('adicionar_feitico.html')

@app.route('/alunos', methods=['GET'])
def alunos():
    return render_template('alunos.html')

@app.route('/editar_aluno/<int:id>', methods=['GET'])
def editar_aluno_render(id):
    return render_template('editar_aluno.html')

@app.route('/adicionar_aluno', methods=['GET'])
def adicionar_aluno_render():
    return render_template('adicionar_aluno.html')

@app.route('/disciplinas', methods=['GET'])
def disciplinas():
    return render_template('disciplinas.html')

@app.route('/editar_disciplina/<int:id>', methods=['GET'])
def editar_disciplina_render(id):
    return render_template('editar_disciplina.html')

@app.route('/adicionar_disciplina', methods=['GET'])
def adicionar_disciplina_render():
    return render_template('adicionar_disciplina.html')

app.add_url_rule('/api/professores', 'listar_professores', professor_controller.listar_professores, methods=['GET'])
app.add_url_rule('/api/professores', 'adicionar_professor', professor_controller.adicionar_professor, methods=['POST'])
app.add_url_rule('/api/professores/<int:professor_id>', 'editar_professor', professor_controller.editar_professor, methods=['PUT'])
app.add_url_rule('/api/professores/<int:professor_id>', 'excluir_professor', professor_controller.excluir_professor, methods=['DELETE'])
app.add_url_rule('/api/professores/<int:professor_id>', 'obter_professor', professor_controller.obter_professor, methods=['GET'])


app.add_url_rule('/api/feiticos', 'listar_feiticos', feitico_controller.listar_feiticos, methods=['GET'])
app.add_url_rule('/api/feiticos', 'adicionar_feitico', feitico_controller.adicionar_feitico, methods=['POST'])
app.add_url_rule('/api/feiticos/<int:feitico_id>', 'editar_feitico', feitico_controller.editar_feitico, methods=['PUT'])
app.add_url_rule('/api/feiticos/<int:feitico_id>', 'excluir_feitico', feitico_controller.excluir_feitico, methods=['DELETE'])

app.add_url_rule('/api/alunos', 'listar_alunos', aluno_controller.listar_alunos, methods=['GET'])
app.add_url_rule('/api/alunos', 'adicionar_aluno', aluno_controller.adicionar_aluno, methods=['POST'])
app.add_url_rule('/api/alunos/<int:aluno_id>', 'editar_aluno', aluno_controller.editar_aluno, methods=['PUT'])
app.add_url_rule('/api/alunos/<int:aluno_id>', 'excluir_aluno', aluno_controller.excluir_aluno, methods=['DELETE'])
app.add_url_rule('/api/alunos/<int:aluno_id>', 'obter_aluno', aluno_controller.obter_aluno, methods=['GET'])

app.add_url_rule('/api/disciplinas', 'listar_disciplinas', disciplina_controller.listar_disciplinas, methods=['GET'])
app.add_url_rule('/api/disciplinas', 'adicionar_disciplina', disciplina_controller.adicionar_disciplina, methods=['POST'])
app.add_url_rule('/api/disciplinas/<int:disciplina_id>', 'editar_disciplina', disciplina_controller.editar_disciplina, methods=['PUT'])
app.add_url_rule('/api/disciplinas/<int:disciplina_id>', 'excluir_disciplina', disciplina_controller.excluir_disciplina, methods=['DELETE'])

app.add_url_rule('/api/casas', 'listar_casas', casa_controller.listar_casas, methods=['GET'])
