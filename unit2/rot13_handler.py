# developed by: Kuksov Pavel
# e-mail: aimed.fire@gmail.com

import webapp2
import utils
from rot13_coder import ROT13Coder


form = """
<head>
<title>Rot13 Encoder/Decoder</title>
</head>
<body>
<form method="post">
    <h1>ROT13 Encoder/Decoder</h1>
    <textarea name="text" cols="80" rows="20">%(text)s</textarea>
    <br>
    <br>
    <input type="submit" value="submit">
</form>
</body>
"""

class ROT13Handler(webapp2.RequestHandler):

    def write_form(self, text=""):
        self.response.write(form % {'text': utils.escape_html(text)})

    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.write_form()

    def post(self):
        original_text = self.request.get('text')
        encoded_text = ROT13Coder().encode(original_text)
        self.write_form(encoded_text)
