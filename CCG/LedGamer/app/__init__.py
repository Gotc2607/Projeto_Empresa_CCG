import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .config import Config
from werkzeug.security import generate_password_hash

# Inicialização das extensões (fora do factory para uso em modelos)
db = SQLAlchemy()
login_manager = LoginManager()

def create_app(config_class=Config):
    """Factory de criação da aplicação Flask"""
    
    # Configuração básica do app
    app = Flask(__name__,
               template_folder='templates',
               static_folder='static',
               instance_relative_config=True)
    
    # Carrega configurações
    app.config.from_object(config_class)
    
    # Configuração de pastas
    os.makedirs(os.path.join(app.instance_path, 'uploads'), exist_ok=True)
    
    # Inicialização de extensões
    initialize_extensions(app)
    
    # Registro de blueprints
    register_blueprints(app)
    
    # Configuração de handlers de erro
    register_error_handlers(app)
    
    # Comandos CLI (opcional)
    register_commands(app)
    
    # Criação de tabelas no banco de dados
    with app.app_context():
        db.create_all()
        create_default_data()  # Opcional: dados iniciais
    
    return app

def initialize_extensions(app):
    """Configura todas as extensões Flask"""
    db.init_app(app)
    
    login_manager.init_app(app)
    login_manager.login_view = 'auth.tela_login'
    login_manager.login_message = 'Por favor, faça login para acessar esta página.'
    login_manager.login_message_category = 'info'
    
    # Outras extensões podem ser adicionadas aqui

def register_blueprints(app):
    """Registra todos os blueprints da aplicação"""
    from app.routes import main_bp
    from app.controllers import auth_bp, produto_bp
    
    # Blueprints principais
    app.register_blueprint(main_bp)
    
    # Blueprints com prefixos
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(produto_bp, url_prefix='/produtos')
    
    # Outros blueprints podem ser adicionados aqui

def register_error_handlers(app):
    """Registra handlers de erro personalizados"""
    
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/404.html'), 404
    
    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('errors/500.html'), 500

def register_commands(app):
    """Registra comandos CLI personalizados"""
    
    @app.cli.command('init-db')
    def init_db():
        """Inicializa o banco de dados"""
        db.create_all()
        print('Banco de dados inicializado.')

def create_default_data():
    """Cria dados iniciais (opcional)"""
    from app.models import Usuario
    
    if not Usuario.query.first():
        admin = Usuario(
            email='admin@example.com',
            nome='Admin',
            senha=generate_password_hash('admin123')
        )
        db.session.add(admin)
        db.session.commit()
        print('Usuário admin criado.')