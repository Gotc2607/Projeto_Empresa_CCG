from flask import Flask
from app.controllers.applications import Applications

app = Flask(__name__, template_folder = 'app/html', static_folder = 'app/statics') #intaciando a classe do Flask
ctl = Applications()

@app.route('/') #decorator que define a rota
def index():
    return ctl.render('pagina_inicial.html') #retorna o template pagina_inicial.html


if __name__ == '__main__':
    app.run(port=5000, debug=True) #inicia o servidor