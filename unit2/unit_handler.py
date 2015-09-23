# developed by: Kuksov Pavel
# e-mail: aimed.fire@gmail.com


import webapp2

form = """
<ul>
    <li><a href="/unit2/rot13">rot13 coder</a></li>
    <li><a href="/unit2/signup">signup page</a></li>
</ul>
"""

class Unit2Handler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(form)
