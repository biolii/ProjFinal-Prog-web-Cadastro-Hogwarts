from flask import Blueprint, jsonify, request, render_template, redirect, url_for, flash, session
from .models import Aluno, User, db
from werkzeug.security import check_password_hash, generate_password_hash

main = Blueprint('main', __name__)

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            session['user_id'] = user.id
            return redirect(url_for('main.home'))
        flash('Usuário ou senha inválidos')
    return render_template('login.html')

@main.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('main.login'))

@main.route('/api/alunos', methods=['GET'])
def api_list_alunos():
    alunos_list = Aluno.query.all()
    alunos = [
        {'id': aluno.id, 'nome': aluno.nome, 'casa': aluno.casa, 'ano': aluno.ano, 'especialidades': aluno.especialidades}
        for aluno in alunos_list
    ]
    return jsonify(alunos)

@main.route('/alunos', methods=['GET'])
def show_alunos():
    alunos_list = Aluno.query.all()
    return render_template('alunos.html', alunos=alunos_list)

@main.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        data = request.get_json(force=True) 
        if not data:
            return jsonify({'message': 'No JSON payload provided'}), 400
        try:
            novo_aluno = Aluno(nome=data['nome'], casa=data['casa'], ano=data['ano'], especialidades=data.get('especialidades', ''))
            db.session.add(novo_aluno)
            db.session.commit()
            return jsonify({'message': 'Aluno adicionado com sucesso!'}), 201
        except Exception as e:
            return jsonify({'message': 'Erro ao salvar no banco de dados', 'error': str(e)}), 500
    else:
        return render_template('cadastrar.html')

@main.route('/')
def home():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('main.login'))
    return render_template('home.html')

@main.route('/alunos/<int:id>/edit', methods=['GET'])
def edit_aluno(id):
    aluno = Aluno.query.get_or_404(id)
    return render_template('edit_aluno.html', aluno=aluno)

@main.route('/alunos/<int:id>/update', methods=['POST'])
def update_aluno(id):
    aluno = Aluno.query.get_or_404(id)
    aluno.nome = request.form['nome']
    aluno.casa = request.form['casa']
    aluno.ano = request.form['ano']
    aluno.especialidades = request.form['especialidades']
    db.session.commit()
    return redirect('/alunos')


@main.route('/alunos/<int:id>/delete', methods=['POST'])
def delete_aluno(id):
    aluno = Aluno.query.get_or_404(id)
    db.session.delete(aluno)
    db.session.commit()
    return redirect ('/alunos')