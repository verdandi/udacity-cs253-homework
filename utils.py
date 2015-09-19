# developed by: Kuksov Pavel
# e-mail: aimed.fire@gmail.com

import cgi

def valid_month(month):
    months = ['January',
              'February',
              'March',
              'April',
              'May',
              'June',
              'July',
              'August',
              'September',
              'October',
              'November',
              'December']

    if month:
        month = month.capitalize()
        if month in months:
            return month

def valid_day(day):
    if day and day.isdigit():
        day = int(day)
        if day >= 1 and day <= 31:
            return day

def valid_year(year):
    if year and year.isdigit():
        year = int(year)
        if year >= 1900 and year <= 2020:
            return year

def escape_html(s):
    return cgi.escape(s, quote=True)
