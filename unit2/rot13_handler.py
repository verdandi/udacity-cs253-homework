# developed by: Kuksov Pavel
# e-mail: aimed.fire@gmail.com

import utils
from rot13_coder import ROT13Coder

class ROT13Handler(utils.Handler):
    def write_form(self, text=""):
        self.render('rot13_form.html', text=text)

    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.write_form()

    def post(self):
        original_text = self.request.get('text')
        encoded_text = ROT13Coder().encode(original_text)
        self.write_form(encoded_text)
