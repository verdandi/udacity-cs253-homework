# developed by: Kuksov Pavel
# e-mail: aimed.fire@gmail.com


import utils

class Unit2Handler(utils.Handler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.render("unit2_form.html")
