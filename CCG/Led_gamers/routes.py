from flask import Flask, request, jsonify, render_template
from app.controllers.application import Applications

app = Flask(__name__, template_folder='app/html', static_folder='app/statics')
ctl = Applications()


@app.route('/')
def index():
    return ctl.render('index')  # Chama Applications.index()
    
@app.route('/login', methods=['POST'])
def login():
    return ctl.render('login')  # Chama Applications.login()

@app.route('/cadastro', methods=['POST'])
def cadastro():
    return ctl.render('cadastro')  # Chama Applications.cadastro()

@app.route('/tela_produtos')
def tela_produtos():
    return ctl.render('tela_produtos')  # Ou render_template diretamente

if __name__ == '__main__':
    app.run(port=5002 ,debug=True)