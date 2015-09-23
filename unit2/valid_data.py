# developed by: Kuksov Pavel
# e-mail: aimed.fire@gmail.com


import re

class DataValidator:
    USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
    PASSWORD_RE = re.compile(r"^.{3,20}$")
    EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")

    def valid_username(self, username):
        return DataValidator.USER_RE.match(username)

    def valid_password(self, password):
        return DataValidator.PASSWORD_RE.match(password)

    def valid_email(self, email):
        if not email: return True

        return DataValidator.EMAIL_RE.match(email)
