# developed by: Kuksov Pavel
# e-mail: aimed.fire@gmail.com

import utils

class ThanksMashkaHandler(utils.Handler):
    def write_form(self):
        self.render("thanks_mashka.html")

    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.write_form()
