# developed by: Kuksov Pavel
# e-mail: aimed.fire@gmail.com

import webapp2
from unit1.unit_handler import Unit1Handler
from unit1.thanks_handler import ThanksHandler
from unit1.mashka_thanks_handler import ThanksMashkaHandler

form = """<a href="/unit1">unit1</a>"""

class MainPageHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(form)


app = webapp2.WSGIApplication([('/', MainPageHandler),
                               ('/unit1', Unit1Handler),
                               ('/unit1/thanks', ThanksHandler),
                               ('/unit1/thanks_mashka', ThanksMashkaHandler),
                              ],
                               debug=False)
