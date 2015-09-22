# developed by: Kuksov Pavel
# e-mail: aimed.fire@gmail.com

import webapp2
import utils
import valid_date


form = """
<form method="post">
    <div style="color: red">%(error)s</div>
    What's your birthday?
    <br>
    <label>
        month
        <input type="text" name="month" value = "%(month)s">
    </label>
    <br>
    <label>
        day
        <input type="text" name="day" value = "%(day)s">
    </label>
    <br>
    <label>
        year
        <input type="text" name="year" value = "%(year)s">
    </label>
    <br>
    <br>
    <input type="submit">
</form>
"""

class Unit1Handler(webapp2.RequestHandler):
    def write_form(self, error="", month="", day="", year=""):
        self.response.write(form % {'error': error,
                                    'month': utils.escape_html(month),
                                    'day': utils.escape_html(day),
                                    'year': utils.escape_html(year)})

    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.write_form()

    def post(self):
        userMonth = self.request.get('month')
        userDay = self.request.get('day')
        userYear = self.request.get('year')
        month = valid_date.valid_month(userMonth)
        day = valid_date.valid_day(userDay)
        year = valid_date.valid_year(userYear)

        if not (month and day and year):
            self.write_form("I'm sorry... You input invalid data :(", userMonth, userDay, userYear)
        else:
            if month == 'October' and day == 15 and year == 1987:
                self.redirect("/unit1/thanks_mashka")
            else:
                self.redirect("/unit1/thanks")
