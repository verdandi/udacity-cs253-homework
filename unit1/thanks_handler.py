# developed by: Kuksov Pavel
# e-mail: aimed.fire@gmail.com

import webapp2

class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("Thanks for your valid data!")
