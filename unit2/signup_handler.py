# developed by: Kuksov Pavel
# e-mail: aimed.fire@gmail.com

import webapp2
import utils
from valid_data import DataValidator


form = """
<!DOCTYPE html>
<html>
<head>
<title>Sign Up</title>
<link rel="stylesheet" href="/styles/style.css" type="text/css">
</head>
<body>
<form method="post">
    <h1>Signup</h1>
    <table>
      <tbody>
        <tr>
          <td class="label">Username</td>
          <td>
            <input type="text" value="%(username)s" name="username"></input>
          </td>
          <td class="error">%(usernameError)s</td>
        </tr>
        <tr>
          <td class="label">Password</td>
          <td>
            <input type="password" value="" name="password"></input>
          </td>
          <td class="error">%(passwordError)s</td>
        </tr>
        <tr>
          <td class="label">Verify Password</td>
          <td>
            <input type="password" value="" name="verify"></input>
          </td>
          <td class="error">%(verifyError)s</td>
        </tr>
        <tr>
          <td class="label">E-Mail (Optional)</td>
          <td>
            <input type="text" value="%(email)s" name="email"></input>
          </td>
          <td class="error">%(emailError)s</td>
        </tr>
      </tbody>
    </table>
    <input type="submit" value="submit">
</form>
</body>
</html>
"""

class SignupHandler(webapp2.RequestHandler):

    def write_form(self, username="", email="", usernameError="", passwordError="", verifyError="", emailError=""):
        self.response.write(form % {'username': utils.escape_html(username),
                                    'email': utils.escape_html(email),
                                    'usernameError': usernameError,
                                    'passwordError': passwordError,
                                    'verifyError': verifyError,
                                    'emailError': emailError
                                    })

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


