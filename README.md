# pythondigest_parser
На основе сайта pythondigest.ru берется по порядку выборка новостей (для примера новости по Python)
В список делаем выборку: дату, заголовок, ссылку на источник, краткое описание.
Соответственно {date, title, link, description}. 
Данные словари по очередно, согласно заданного количества обрабатываемых страниц,
сохраняем в файл data.csv

Используемые библиотеки:
requests, 
from bs4 import BeautifulSoup,  
from csv import DictWriter
