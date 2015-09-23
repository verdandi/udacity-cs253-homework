# developed by: Kuksov Pavel
# e-mail: aimed.fire@gmail.com

import webapp2


class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        username = self.request.get('username')
        self.response.write("<h1>Welcome, %s!</h1>" % username)
