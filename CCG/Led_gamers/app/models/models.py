

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




    def adicionar_usuario(self, nome, senha, email):
        if self.db.adicionar_usuario(nome, senha, email):
            return True
        else:
            return False