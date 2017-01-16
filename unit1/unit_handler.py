# developed by: Kuksov Pavel
# e-mail: aimed.fire@gmail.com

import utils
import valid_date

class Unit1Handler(utils.Handler):
    def write_form(self, error="", month="", day="", year=""):
        self.render("unit1_form.html", error=error, month=month, day=day, year=year)

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
