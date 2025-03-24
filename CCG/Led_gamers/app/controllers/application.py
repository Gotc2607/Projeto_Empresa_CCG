from flask import render_template

class Applications:
    
    def __init__(self):
        self.pages = {
            'pagina_inicial' : self.pagina_inicial,
            'login' : self.login,
            'tela_carrinho' : self.tela_carrinho,
            'tela_produtos' : self.tela_produtos,
        }


    def render(self,page, **kwargs):
       content = self.pages.get(page, self.pagina1)
       return content(**kwargs)

    def pagina_inicial(self):
        return render_template('pagina1.html')

    def login(self):
        return render_template('login.html')

    def tela_carrinho(self):
        return render_template('tela_carrinho.html')

    def tela_produtos(self):
        return render_template('tela_produtos.html')

        