import sqlite3
import bcrypt

class BancoDeDados:

    def __init__(self):
        self.conn = sqlite3.connect('db/database.db')
        self.cursor = self.conn.cursor()
        self.tabela_usuario()
        self.tabela_produto()

    #criar as tabelas
    def tabela_usuario(self):
       self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuario(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                senha TEXT NOT NULL,
                email TEXT NOT NULL
            );
        ''')

    def tabela_produto(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS produto(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                marca TEXT NOT NULL,
                modelo TEXT NOT NULL,
                preco REAL NOT NULL,
                descricao TEXT NOT NULL
            );
        ''')    

    #obter as informações dos usuarios 
    def obter_dados_usuario(self, nome):
        self.cursor.execute('SELECT * FROM usuario WHERE nome = ?', (nome,))
        usuario = self.cursor.fetchone()
        return usuario #vai retornar uma tupla com as informações do usuario

    #obter todos os usuarios
    def obter_todos_usuarios(self):
        self.cursor.execute('SELECT * FROM usuario')
        usuarios = self.cursor.fetchall()
        return usuarios

    #adicionar um novo usuario
    def adicionar_usuario(self, nome, senha, email):
        senha_hash = self.criptografar_senha(senha)
        self.cursor.execute('INSERT INTO usuario (nome, senha, email) VALUES (?, ?, ?)', (nome, senha_hash, email))

    #criptografar a senha
    def criptografar_senha(self, senha):
        senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())
        return senha_hash   

    #verificar se a senha é a mesma que a senha_hash  
    def verificar_senha(self, senha, senha_hash):
        if bcrypt.checkpw(senha.encode(), senha_hash):
            return True
        else:
            return False



    #obter as informações dos produtos
    def obter_produto(self, nome):  
        self.cursor.execute('SELECT * FROM produto WHERE nome = ?', (nome,))
        produto = self.cursor.fetchone()
        return produto

    def obter_todos_produtos(self):
        self.cursor.execute('SELECT * FROM produto')
        produtos = self.cursor.fetchall()
        return produtos

    #adicionar um novo produto
    def adicionar_produto(self, nome, marca, modelo, preco, descricao):
        self.cursor.execute('INSERT INTO produto (nome, marca, modelo, preco, descricao) VALUES (?, ?, ?, ?, ?)', (nome, marca, modelo, preco, descricao))

    