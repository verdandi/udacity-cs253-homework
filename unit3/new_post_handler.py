# developed by: Kuksov Pavel
# e-mail: aimed.fire@gmail.com

import utils
from article import Article

class NewPostHandler(utils.Handler):
    def write_form(self, title = "", article = "", error = ""):
        self.render('new_post_form.html', title = title, article = article, error = error)

    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.write_form()

    def post(self):
        title = self.request.get('subject')
        article = self.request.get('content')
        if title and article:
            new_article = Article(title = title, article = article)
            new_article.put()
            self.redirect("/unit3/%s" % new_article.key().id())
        else:
            self.write_form(title, article, "you should fill both fields: 'title' and 'article'")


