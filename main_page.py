# developed by: Kuksov Pavel
# e-mail: aimed.fire@gmail.com

import webapp2

from unit1.unit_handler import Unit1Handler
from unit1.thanks_handler import ThanksHandler
from unit1.mashka_thanks_handler import ThanksMashkaHandler
from unit2.unit_handler import Unit2Handler
from unit2.rot13_handler import ROT13Handler
from unit2.signup_handler import SignupHandler

form = """
<ul>
    <li><a href="/unit1">unit1</a></li>
    <li><a href="/unit2">unit2</a></li>
    <ul>
        <li><a href="/unit2/rot13">rot13 coder</a></li>
        <li><a href="/unit2/signup">signup page</a></li>
    </ul>
</ul>
"""

class MainPageHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(form)


app = webapp2.WSGIApplication([('/', MainPageHandler),
                               ('/unit1', Unit1Handler),
                               ('/unit1/thanks', ThanksHandler),
                               ('/unit1/thanks_mashka', ThanksMashkaHandler),
                               ('/unit2', Unit2Handler),
                               ('/unit2/rot13', ROT13Handler),
                               ('/unit2/signup', SignupHandler),
                              ],
                               debug=False)
