from flask import render_template

class Applications:
    
    def __init__(self):
        self.pages = {
            'pagina1' : self.pagina1,
        }


    def render(self,page, **kwargs):
       content = self.pages.get(page, self.pagina1)
       return content(**kwargs)

    def pagina1(self):
        return render_template('pagina1.html')