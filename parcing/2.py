import requests
from bs4 import BeautifulSoup
import json

def yandex_chart(url):

    r = requests.get(url)
    page = BeautifulSoup(r.text, 'lxml')

    singer = page.findAll('div', attrs = {'class': 'd-track__meta'})

    track = page.findAll('div', attrs = {'class' : 'd-track__name'})

    res = {i + 1 : {singer[i].text : ' '.join(track[i].text.split())} for i in range(len(track))}

    with open ('chart.json', 'w', encoding = 'utf-8') as f:
        json.dump(res, f, ensure_ascii=False)



yandex_chart('https://music.yandex.ru/chart')