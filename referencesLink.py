from bs4 import BeautifulSoup
import requests
from htmldate import find_date
import re
from datetime import datetime


url = input("Please enter your URL: ")
html = requests.get(url).content.decode('utf-8')
date = find_date(html)
year = date[:4]
day = date[8:10]


def get_web_name():
    pattern = re.compile(r'(https?://|www\.)?(www\.)?([a-z0-9-]+)(\..+)?')
    subbed_url = pattern.sub(r'\3', url)
    return subbed_url


def get_date():
    return month(date, year, day)


def get_title():
    # making requests instance
    reqs = requests.get(url)

    # using the BeautifulSoup module
    soup = BeautifulSoup(reqs.text, 'html.parser')
    web_title = ""
    # displaying the title
    for title in soup.find_all('title'):
        web_title = title.get_text()

    return web_title


def month(num_string, year, day):
    month_number = str(num_string[5:7])
    month_string = ""
    if month_number == "01":
        month_string = "January"
    elif month_number == "02":
        month_string = "February"
    elif month_number == "03":
        month_string = "March"
    elif month_number == "04":
        month_string = "April"
    elif month_number == "05":
        month_string = "May"
    elif month_number == "06":
        month_string = "June"
    elif month_number == "07":
        month_string = "July"
    elif month_number == "08":
        month_string = "August"
    elif month_number == "09":
        month_string = "September"
    elif month_number == "10":
        month_string = "October"
    elif month_number == "11":
        month_string = "November"
    else:
        month_string = "December"

    return day + " " + month_string + " " + year


def give_all():
    reference = get_web_name() + ". " + year + ". " + get_title() + ", " + get_date() + ". [Online]. Available at: " + url + "[Accessed " + datetime.today().date()
    return reference


print(give_all())
