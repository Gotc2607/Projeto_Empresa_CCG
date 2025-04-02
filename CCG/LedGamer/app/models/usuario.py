from app import db, login_manager
from flask_login import UserMixin

class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(60), nullable=False)
    nome = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Usuário('{self.email}', '{self.nome}')"

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))