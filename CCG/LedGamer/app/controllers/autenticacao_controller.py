from flask import Blueprint, request, flash, redirect, url_for, render_template
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from app.models.usuario import Usuario
from app import db

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')  # Adicionado url_prefix

@auth_bp.route('/tela_login', methods=['GET'])
def tela_login():
    return render_template('auth/tela_login.html')

@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        nome = request.form.get('nome')
        senha = request.form.get('senha')
        
        if not nome or not senha:
            flash('Preencha todos os campos', 'error')
            return redirect(url_for('auth.tela_login'), message='Preencha todos os campos')

        
        usuario = Usuario.query.filter_by(nome=nome).first()
        
        if not usuario or not check_password_hash(usuario.senha, senha):
            flash('Credenciais inválidas', 'error')
            return redirect(url_for('auth.tela_login'), message='Credenciais inválidas')
        
        login_user(usuario)
        flash('Login realizado com sucesso!', 'success')
        return redirect(url_for('main.index'))
    
    except Exception as e:
        flash('Erro durante o login', 'error')
        return redirect(url_for('auth.tela_login'))

@auth_bp.route('/cadastro', methods=['POST'])
def cadastro():
    try:
        email = request.form.get('email')
        nome = request.form.get('nome')
        senha = request.form.get('senha')
        
        if not all([email, nome, senha]):
            flash('Preencha todos os campos', 'error')
            return redirect(url_for('auth.tela_login'), message='Preencha todos os campos')
        
        if Usuario.query.filter_by(email=email).first():
            flash('Email já cadastrado', 'error')
            return redirect(url_for('auth.tela_login'), message='Email já cadastrado')
        
        novo_usuario = Usuario(
            email=email,
            nome=nome,
            senha=generate_password_hash(senha, method='pbkdf2:sha256')
        )
        
        db.session.add(novo_usuario)
        db.session.commit()
        
        flash('Cadastro realizado com sucesso! Faça login.', 'success')
        return redirect(url_for('auth.tela_login'))
    
    except Exception as e:
        db.session.rollback()
        flash('Erro durante o cadastro', 'error')
        return redirect(url_for('auth.tela_login'))

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Você foi desconectado', 'info')
    return redirect(url_for('auth.tela_login'))