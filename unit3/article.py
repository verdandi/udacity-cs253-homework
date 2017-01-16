# developed by: Kuksov Pavel
# e-mail: aimed.fire@gmail.com

from google.appengine.ext import db

class Article(db.Model):
    title = db.TextProperty(required = True)
    article = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)

    def get_text(self):
        return self.article.replace('\n','<br>')
