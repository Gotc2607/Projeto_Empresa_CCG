from flask import Flask
from app.controllers.application import Applications
from flask_jwt_extended import JWTManager

app = Flask(__name__, template_folder = 'app/html', static_folder = 'app/statics') #intaciando a classe do Flask
app.config["JWT_SECRET_KEY"] = "CCG--chave_de_acesso"  # Use uma chave forte
jwt = JWTManager(app)
ctl = Applications()

@app.route('/') #decorator que define a rota
def index():
    return ctl.render('pagina1.html') #retorna o template pagina_inicial.html


if __name__ == '__main__':
    app.run(port=5002, debug=True) #inicia o servidor