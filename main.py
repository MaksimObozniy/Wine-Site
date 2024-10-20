from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from collections import defaultdict
import datetime
import pandas
import pprint

excel_data = pandas.read_excel("wine3.xlsx", sheet_name='Лист1', usecols=['Категория', 'Название', 'Сорт', 'Цена', 'Картинка', 'Акция'])
excel_data = excel_data.where(pandas.notnull(excel_data), None)
excel_data_list = excel_data.to_dict(orient='records')

grouped_data = defaultdict(list)
for wine in excel_data_list:
    grouped_data[wine['Категория']].append(wine)


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

now = datetime.datetime.now()
age_of_winery = now.year - 1921


def get_year_suffix(year):
    if 11 <= year % 100 <= 19:
        return "лет"
    last_digit = year % 10
    if last_digit == 1:
        return "год"
    elif 2 <= last_digit <= 4:
        return "года"
    else:
        return "лет"


year_suffix = get_year_suffix(age_of_winery)

rendered_page = template.render(wines=excel_data_list, grouped_data=grouped_data, year_suffix=year_suffix, age_of_winery=age_of_winery)

with open('index.html', 'w', encoding="utf8") as f:
    f.write(rendered_page)
    
server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()

