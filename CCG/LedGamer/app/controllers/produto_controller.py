from flask import Blueprint, render_template, flash, redirect, url_for
from app.models.produto import Produto
from app import db

produto_bp = Blueprint('produto', __name__, url_prefix='/produtos')

@produto_bp.route('/produtos', methods=['GET'])
def listar():
    try:
        produtos = Produto.query.all()
        return render_template('produtos/lista.html', produtos=produtos)
    except Exception as e:
        flash('Erro ao carregar produtos', 'error')
        return redirect(url_for('main.index'))

@produto_bp.route('/<int:id>')
def detalhes(id):
    try:
        produto = Produto.query.get_or_404(id)
        return render_template('produtos/detalhes.html', produto=produto)
    except Exception as e:
        flash('Produto não encontrado', 'error')
        return redirect(url_for('produto.listar'))