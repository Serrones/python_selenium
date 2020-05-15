"""
Pegar todos os links de aulas

Navegar até o exercício 03

"""

from time import sleep
from selenium.webdriver import Firefox
from pprint import pprint

from aula_04_b import find_by_text

url = 'https://selenium.dunossauro.live/aula_04.html'

browser = Firefox()

browser.get(url)

# Pegar todos os links de aulas
aside = browser.find_element_by_tag_name('aside')
sleep(0.50)
aside_anchors = aside.find_elements_by_tag_name('a')

anchors = dict()
for anchor in aside_anchors:
    anchors[anchor.text] = anchor.get_attribute("href")
pprint(anchors)

# Navegar até o exercício 03

tag_main = browser.find_element_by_tag_name('main')

sleep(0.50)

exercise = find_by_text('Exercício 3', tag_main, 'a')

exercise.click()

sleep(0.50)

print(f'Você está em {browser.title}: {browser.current_url}')

sleep(1.50)

browser.back()

sleep(0.50)

print(f'Agora você voltou para {browser.title}: {browser.current_url}')
