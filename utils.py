# developed by: Kuksov Pavel
# e-mail: aimed.fire@gmail.com

import webapp2
import jinja2
import os

import cgi

def escape_html(s):
    return cgi.escape(s, quote=True)


class Handler(webapp2.RequestHandler):
    template_dir = os.path.join(os.path.dirname(__file__), 'templates')
    jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

    def write(self, *unnamed_args, **named_args):
        self.response.out.write(*unnamed_args, **named_args)

    def render_str(self, template, **params):
        t = self.jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **params):
        self.write(self.render_str(template, **params))
