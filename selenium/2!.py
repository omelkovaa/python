"""
Напишите программу которая автоматически собирает ваше расписание в Элжуре. и сохраняет в json файл в виде:
{день недели: {Предмет: Аудитория}
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import lxml
import json
import time

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

driver.get('https://class.sirius.ru/authorize')

s_search = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div[1]/form/div[1]/div[1]/div/input')
s_search.clear()
s_search.send_keys('логин')

s_search = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div[1]/form/div[1]/div[2]/div/input')
s_search.clear()
s_search.send_keys('пароль')

s_search.send_keys(Keys.ENTER)
time.sleep(1)
s_search = driver.find_element(By.XPATH, '/html/body/div[1]/div/header/div/div/div/nav/div/a[4]')
s_search.click()
time.sleep(1)

class_data = {}

page_source = driver.page_source
soup = BeautifulSoup(page_source, 'lxml')
#делаем контейнер со всеми блоками дней(schedule__day)
days = soup.find_all('div', 'schedule__day')

#проходимся циклом по контейнеру с днями
for day in days:
    #создаем словарь с ключами под наименование дней недели(column-40) с пустым словарем вместо значения
    class_data[day.find("div", "column-40").text.strip()] = {}
    #записываем все блоки пар в переменную
    lessons = day.find_all("div", "columns")
    #проходимся циклом по каждому блоку пары
    for j in range(1,len(lessons)):
        lesson = lessons[j]
        if lesson.find('span','schedule-lesson') != None:
            if 'L1' in lesson.find('span','schedule-lesson').text.strip() or 'L3' in lesson.find('span','schedule-lesson').text.strip():
                continue
            else:
                class_data[day.find("div", "column-40").text.strip()][lesson.find('span','schedule-lesson').text.strip()] = lesson.find('div', 'schedule__day__content__lesson__room').text.strip()

with open('class.json', 'w', encoding="utf-8") as f:
    json.dump(class_data, f, indent=4, ensure_ascii=False)


# 1. Импортируются необходимые библиотеки: selenium, BeautifulSoup, By, Options и json из соответствующих модулей.
# 2. Создаются объекты webdriver и options для запуска браузера Chrome.
# 3. Открывается сайт Элжура и производится авторизация с помощью логина и пароля.
# 4. Находится кнопка "Расписание" на странице и происходит переход на страницу с расписанием.
# 5. Получается исходный код страницы и передается в объект BeautifulSoup для парсинга.
# 6. Извлекаются все элементы div с классом "schedule__day", которые содержат информацию о расписании на определенный день недели.
# 7. Для каждого дня создается словарь вида {Предмет: Аудитория}, где ключом является название предмета, а значением - номер аудитории.
# 8. Словарь для каждого дня добавляется в словарь class_data с ключом, соответствующим дню недели.
# 9. Полученный словарь сохраняется в файл class.json в формате json с отступами и без использования ASCII-символов.