"""
Напишите программу которая автоматически зайдет на https://store.steampowered.com/ в поле поиска отправит стратегии
и соберет названия всех стратегий на 1 странице.
"""
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

options = Options()
driver = webdriver.Chrome(options=options)
driver.get("https://store.steampowered.com/")
search = driver.find_element(By.XPATH,
                             "//*[@id=\"store_nav_search_term\"]")

search.send_keys("Стратегии")
search.send_keys(Keys.ENTER)

page_source = driver.page_source
soup = BeautifulSoup(page_source, "lxml")
name = soup.find_all("div", "responsive_search_name_combined")
k = 1
for i in name:
    title = i.find("span", "title").text
    print(f"{k} место: {title}")
    k += 1

#
# 1. Импортируются необходимые библиотеки: selenium,
# BeautifulSoup, By и Options из модуля selenium.webdriver.common.
# 2. Создаются объекты webdriver и options для запуска браузера Chrome.
# 3. Открывается сайт Steam.
# 4. Находится поле поиска на странице и вводится запрос "Стратегии".
# 5. Получается исходный код страницы и передается в объект BeautifulSoup для парсинга.
# 6. Извлекаются все элементы div с классом "responsive_search_name_combined", которые содержат информацию о
# названии и других характеристиках игр.
# 7. Для каждого элемента извлекается название игры (элемент span с классом "title") и
# выводится на экран вместе с порядковым номером.
# 8. Код не учитывает случай, когда на странице больше одной страницы с результатами поиска,
# и не реализует автоматическое переключение на следующую страницу.