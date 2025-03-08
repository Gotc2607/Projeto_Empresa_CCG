from flask import  render_template

class Applications:

    def __init__(self):
        self.pages = {
            'pagina_inicial' : self.pagina_inicial,
        }


    def render(self,page, **kwargs):
       content = self.pages.get(page, self.pagina_inicial)
       return content(**kwargs)

    def pagina_inicial(self):
        return render_template('pagina_inicial.html')   