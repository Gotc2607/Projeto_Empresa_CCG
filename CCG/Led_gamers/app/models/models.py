from app.models.banco import BancoDeDados

class Usuario:
    def __init__(self, nome, senha, email):
        self.nome = nome
        self.senha = senha
        self.email = email

class Produto:
    def __init__(self, nome, marca ,preco, descricao):
        self.nome = nome
        self.marca = marca
        self.preco = preco
        self.descricao = descricao

class Model:
    def __init__(self):
        self.db = BancoDeDados()



    #cadastro de novos usuarios
    def cadastro(self, nome, senha, email):
        if not self.db.verificar_usuario(nome):
            senha_hash = self.db.criptografar_senha(senha)
            self.db.adicionar_usuario(nome, senha_hash, email)

            return True
        else:
            return False

    #login dos usuarios
    def login(self, nome, senha):
        if autenticar_usuario(nome, senha):
            return True
        else:
            return False