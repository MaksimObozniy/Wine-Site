from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from collections import defaultdict
import datetime
import pandas
import argparse


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


def main():
    
    parser = argparse.ArgumentParser(description="Программа для изменение винной картотеки и применение акций исходя из данных таблиц Excel")
    parser.add_argument("excel_file_path", type=str, help="Путь к файлу Excel где находится винная карта с ценами, названиями и тд.")
    parser.add_argument("--excel_list_name", type=str, default="Лист1", help="Название страницы в фале Excel. По умолчанию 'Лист1'")
    args = parser.parse_args()
    
    excel_data = pandas.read_excel(args.excel_file_path, 
                                   sheet_name=args.excel_list_name, 
                                   usecols=['Категория', 'Название', 'Сорт', 'Цена', 'Картинка', 'Акция'])
    
    excel_data = excel_data.where(pandas.notnull(excel_data), None)
    wine_data = excel_data.to_dict(orient='records')

    grouped_data = defaultdict(list)
    for wine in wine_data:
        grouped_data[wine['Категория']].append(wine)

    env = Environment(  
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    now = datetime.datetime.now()
    age_of_winery = now.year - 1921

    year_suffix = get_year_suffix(age_of_winery)

    rendered_page = template.render(wines=wine_data, grouped_data=grouped_data, year_suffix=year_suffix, age_of_winery=age_of_winery)

    with open('index.html', 'w', encoding="utf8") as f:
        f.write(rendered_page)
    
    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()

    
if __name__ == '__main__':
    main()
    

