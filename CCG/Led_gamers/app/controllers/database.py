import sqlite3
import bcrypt
from contextlib import contextmanager

class BancoDeDados:

    def __init__(self):
        self.conn = sqlite3.connect('database.db', check_same_thread=False)
        self.conn.row_factory = sqlite3.Row  # Para retornar dicionários
        self.cursor = self.conn.cursor()
        self.criar_tabelas()

    @contextmanager
    def gerenciar_transacao(self):
        try:
            yield
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e

    #criar as tabelas
    def criar_tabelas(self):
        with self.gerenciar_transacao():
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS usuario(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL UNIQUE,
                    senha TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE
                );''')
            
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS produto(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    marca TEXT NOT NULL,
                    modelo TEXT NOT NULL,
                    preco REAL NOT NULL,
                    descricao TEXT NOT NULL
                );''')



    #obter informações de um usuario 
    def obter_usuario(self, nome):
        self.cursor.execute('SELECT * FROM usuario WHERE nome = ?', (nome,))
        usuario = self.cursor.fetchone()
        return usuario

    #obter todos os usuarios
    def obter_todos_usuarios(self):
        self.cursor.execute('SELECT * FROM usuario')
        usuarios = self.cursor.fetchall()
        return usuarios

    #adicionar um novo usuario
    def adicionar_usuario(self, nome, senha, email):
        with self.gerenciar_transacao():
            senha_hash = self.criptografar_senha(senha)
            self.cursor.execute(
                'INSERT INTO usuario (nome, senha, email) VALUES (?, ?, ?)',
                (nome, senha_hash, email)
            )
            return self.cursor.lastrowid

    #criptografar a senha
    def criptografar_senha(self, senha):
        senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())
        return senha_hash   

    #verificar se a senha está correta
    def verificar_senha(self, senha, senha_hash):
        """Verifica se a senha corresponde ao hash armazenado"""
        try:
            # Converte para bytes se necessário (para lidar com hash vindo do banco como string)
            if isinstance(senha_hash, str):
                senha_hash = senha_hash.encode('utf-8')
            
            # Converte a senha para bytes (se ainda não estiver)
            senha_bytes = senha.encode('utf-8') if isinstance(senha, str) else senha
            
            # Retorna True se coincidir, False se não
            return bcrypt.checkpw(senha_bytes, senha_hash)
            
        except Exception:
            return False  # Retorna False em qualquer erro (senha inválida, hash corrompido, etc.)

    #verificar se o usuario existe
    def verificar_usuario(self, nome):
        self.cursor.execute('SELECT * FROM usuario WHERE nome = ?', (nome,))
        usuario = self.cursor.fetchone()
        if usuario:
            return True
        else:
            return False

    #autenticar o usuario
    def autenticar_usuario(self, nome, senha):
        usuario = self.obter_usuario(nome=nome)
        if not usuario:
            return False
        return self.verificar_senha(senha, usuario['senha'])

    def email_existe(self, email):
        self.cursor.execute('SELECT 1 FROM usuario WHERE email = ?', (email,))
        return bool(self.cursor.fetchone())



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
        with self.gerenciar_transacao():  # Adicionado gerenciador de transação
            self.cursor.execute(
                'INSERT INTO produto (nome, marca, modelo, preco, descricao) VALUES (?, ?, ?, ?, ?)',
                (nome, marca, modelo, preco, descricao)
            )
            return self.cursor.lastrowid

    