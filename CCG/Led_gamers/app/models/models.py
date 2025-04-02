from app.controllers.database import BancoDeDados

class Usuario:
    def __init__(self, id, nome, senha, email):
        self.id = id
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
        senha_hash = self.db.criptografar_senha(senha)
        # Verifica se o usuário já existe   
        if not self.db.verificar_usuario(nome):
            self.db.adicionar_usuario(nome, senha_hash, email)
            print('usuario cadastrado')
            return True
        print('falha no cadastro')
        return False

    #login dos usuarios
    def login(self, nome, senha):
        usuario = self.db.obter_usuario(nome)
        print('usuario encontrado:')
        if usuario:
            # Verifica se a senha está correta
            if self.db.verificar_senha(senha, usuario['senha']):
                print('senha correta')
                return True
            else:
                print('senha incorreta')
                return False
        else:
            return False
    #ober dados do usuario
    def obter_dados_usuario(self, nome):
        try:
            usuario = self.db.obter_usuario(nome=nome)
            if usuario:
                return {
                    'success': True,
                    'user': dict(usuario)  # Converte Row para dicionário
                }
            return {'success': False, 'message': 'Usuário não encontrado'}
        except Exception as e:
            return {
                'success': False,
                'message': f'Erro ao obter usuário: {str(e)}'
            }