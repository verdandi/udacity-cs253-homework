# developed by: Kuksov Pavel
# e-mail: aimed.fire@gmail.com

import utils
from article import Article

class ArticleHandler(utils.Handler):
    def write_form(self,article = None):
        self.render('article_form.html', article = article)

    def get(self, page_id):
        self.response.headers['Content-Type'] = 'text/html'
        self.write_form(Article.get_by_id(int(page_id)))
