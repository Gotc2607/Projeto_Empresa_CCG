from flask import render_template

class Applications:
    
    def __init__(self):
        self.pages = {
            'pagina2' : self.pagina2,
        }


    def render(self,page, **kwargs):
       content = self.pages.get(page, self.pagina2)
       return content(**kwargs)

    def pagina2(self):
        return render_template('pagina2.html')