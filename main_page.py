# developed by: Kuksov Pavel
# e-mail: aimed.fire@gmail.com

import utils
# import re

from unit1.unit_handler import Unit1Handler
from unit1.thanks_handler import ThanksHandler
from unit1.mashka_thanks_handler import ThanksMashkaHandler
from unit2.unit_handler import Unit2Handler
from unit2.rot13_handler import ROT13Handler
from unit2.signup_handler import SignupHandler
from unit2.welcome_handler import WelcomeHandler
from unit3.unit_handler import Unit3Handler
from unit3.new_post_handler import NewPostHandler
from unit3.article_handler import ArticleHandler


class MainPageHandler(utils.Handler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.render("main_page.html")


app = utils.webapp2.WSGIApplication([('/', MainPageHandler),
                               ('/unit1', Unit1Handler),
                               ('/unit1/', Unit1Handler),
                               ('/unit1/thanks', ThanksHandler),
                               ('/unit1/thanks_mashka', ThanksMashkaHandler),
                               ('/unit2', Unit2Handler),
                               ('/unit2/', Unit2Handler),
                               ('/unit2/rot13', ROT13Handler),
                               ('/unit2/signup', SignupHandler),
                               ('/unit2/welcome', WelcomeHandler),
                               ('/unit3', Unit3Handler),
                               ('/unit3/', Unit3Handler),
                               ('/unit3/newpost', NewPostHandler),
                               (r'/unit3/([0-9]+)', ArticleHandler),
                              ],
                               debug=True)
