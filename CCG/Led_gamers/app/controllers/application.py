from flask import render_template, request, redirect, jsonify
from app.models.models import Model
from datetime import timedelta
from flask_jwt_extended import create_access_token

class Applications:
    
    def __init__(self):
        self.pages = {
            'pagina_inicial' : self.pagina_inicial,
            'login' : self.login,
            'tela_carrinho' : self.tela_carrinho,
            'tela_produtos' : self.tela_produtos,
        }
        self.model = Model()    

    def render(self,page, **kwargs):
       content = self.pages.get(page, self.pagina1)
       return content(**kwargs)

    def pagina_inicial(self):
        return render_template('pagina1.html')

    #login dos usuarios
    def login(self):
        if request.method == 'POST':
            nome = request.form.get('nome')
            senha = request.form.get('senha')

            if not nome or not senha:
                return {"success": False, "message": "Preencha todos os campos"}

        
            user = self.model.login(nome, senha)
            if user:
                access_token = create_access_token(identity=nome, expires_delta=timedelta(hours=1))
                return redirect('/tela_produtos')

        return render_template('login.html')

    #cadastro de novos usuarios
    def cadastro(self):
        if request.method == 'POST':
            nome = request.form.get('nome')
            email = request.form.get('email')   
            senha = request.form.get('senha')

            if not nome or not email or not senha:
                return {"success": False, "message": "Preencha todos os campos"}

            cadastro =  self.model.cadastro(nome, senha, email)
            if cadastro:
                return jsonify(result), 201  # Retorna 201 para "Created"
            else:
                return jsonify(result), 400  # Se falhar, retorna erro 400
                
        return render_template('cadastro.html')

    def tela_carrinho(self):
        return render_template('tela_carrinho.html')

    def tela_produtos(self):
        return render_template('tela_produtos.html')

        