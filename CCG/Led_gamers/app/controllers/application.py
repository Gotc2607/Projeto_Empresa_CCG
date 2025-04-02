from flask import render_template, request, jsonify
from app.models.models import Model

class Applications:
    def __init__(self):
        self.model = Model()
        self.pages = {
            'login': self.login,
            'cadastro': self.cadastro,
            'tela_produtos': self.tela_produtos,
            'index': self.index,
        }

    def render(self, page, **kwargs):
        """Renderiza templates com contexto"""
        return self.pages.get(page, self.login)(**kwargs)


    # ----- Index -----
    def index(self):
        return render_template('index.html')

    # ----- Login -----
    def login(self):
        nome = request.form.get('nome')
        senha = request.form.get('senha')

        if  not nome or not senha:
            return render_template('login.html', error="Preencha todos os campos")

    # ----- Cadastro -----
    def cadastro(self, **kwargs):
        if request.method == 'POST':
            # Processamento AJAX
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                nome = request.form.get('nome')
                senha = request.form.get('senha')
                email = request.form.get('email')
                
                if self.model.cadastro(nome, senha, email):
                    return jsonify({"success": True, "redirect": "/login?cadastro=sucesso"})
                return jsonify({"success": False, "error": "Usuário já existe"})
            
            # Fallback para POST tradicional
            return render_template('login.html', error="Erro no cadastro")
        
        # GET request
        return render_template('login.html', **kwargs)