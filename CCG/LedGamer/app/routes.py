from flask import Blueprint

# Blueprint principal
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """Rota inicial da aplicação"""
    return "Página Inicial"

def init_app(app):
    """
    Registra todos os blueprints na aplicação Flask
    
    Parâmetros:
        app (Flask): Instância da aplicação Flask
    """
    from app.controllers import auth_bp, produto_bp  # Importação tardia para evitar circular imports
    
    # Registra blueprints com prefixos opcionais
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')  # Todas as rotas de auth começam com /auth
    app.register_blueprint(produto_bp, url_prefix='/produtos')  # Rotas de produtos em /produtos
    
    # Opcional: Adicione tratamento de erro 404 personalizado
    @app.errorhandler(404)
    def page_not_found(e):
        return "Página não encontrada", 404