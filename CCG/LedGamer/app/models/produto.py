from app import db

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    descricao = db.Column(db.Text)
    estoque = db.Column(db.Integer, default=0)
    imagem = db.Column(db.String(255))

    def __repr__(self):
        return f'<Produto {self.nome}>'