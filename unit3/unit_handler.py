# developed by: Kuksov Pavel
# e-mail: aimed.fire@gmail.com

import utils
from article import Article
from google.appengine.ext import db

class Unit3Handler(utils.Handler):
    def write_form(self, title = "", article = "", error = ""):
        articles = db.GqlQuery('SELECT * FROM Article ORDER BY created DESC')
        self.render("blog_main_page.html", articles = articles)

    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.write_form()
