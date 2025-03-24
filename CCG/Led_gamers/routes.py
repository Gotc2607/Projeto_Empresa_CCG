from flask import Flask
from app.controllers.application import Applications

app = Flask(__name__, template_folder = 'app/html', static_folder = 'app/statics') #intaciando a classe do Flask
ctl = Applications()

@app.route('/') #decorator que define a rota
def index():
    return ctl.render('pagina1.html') #retorna o template pagina_inicial.html


if __name__ == '__main__':
    app.run(port=5002, debug=True) #inicia o servidor