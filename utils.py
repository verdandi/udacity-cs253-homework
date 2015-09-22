# developed by: Kuksov Pavel
# e-mail: aimed.fire@gmail.com

import cgi


def escape_html(s):
    return cgi.escape(s, quote=True)

