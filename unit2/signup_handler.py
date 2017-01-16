# developed by: Kuksov Pavel
# e-mail: aimed.fire@gmail.com

import utils
from valid_data import DataValidator


class SignupHandler(utils.Handler):

    def write_form(self, username="", email="", usernameError="", passwordError="", verifyError="", emailError=""):
        self.render('signup_form.html', username = username, email = email, usernameError = usernameError,
            passwordError = passwordError, verifyError = verifyError, emailError = emailError)

    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.write_form()

    def post(self):
        self.response.headers['Content-Type'] = 'text/html'

        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')

        usernameError = "" if DataValidator().valid_username(username) else "That's not valid username"
        passwordError = "" if DataValidator().valid_password(password) else "That's not valid password"
        verifyError = "" if password == verify else "Your passwords didn't match"
        emailError = "" if DataValidator().valid_email(email) else "That's not valid email"

        if usernameError or passwordError or verifyError or emailError:
            self.write_form(username, email, usernameError, passwordError, verifyError, emailError)
        else:
            self.redirect("/unit2/welcome?username=%s" % username)


