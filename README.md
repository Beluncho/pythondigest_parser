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

# telegramm bot
На основе парсера сайта pythondigest.ru создаем телеграм ботю Основные команды:                                                          
/start - 'send "/help" for help' 'or text me'                                                                                           
/help - 'send /parsing for news from pythondigest.ru (about python)'                                                                     
         'send /file for data news'                                                                                     
         'send "any text" for revers "txet yna"'                                                                                         
/parsing - 5 последних новостей по теме Python                                                                                           
/file - приходит файл data.csv (сохраненные данные парсера)                                                                              
При написании любохо текста приходит реверс - "any text" - "txet yna"
