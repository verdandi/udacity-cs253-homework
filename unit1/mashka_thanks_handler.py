# developed by: Kuksov Pavel
# e-mail: aimed.fire@gmail.com

import webapp2

class ThanksMashkaHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("Mashka?! O_o")
