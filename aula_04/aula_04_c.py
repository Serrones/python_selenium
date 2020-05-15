from selenium.webdriver import Firefox
from aula_04_b import find_by_text

from time import sleep


url = 'https://selenium.dunossauro.live/aula_04_b.html'

browser = Firefox()

browser.get(url)


boxes = ['um', 'dois', 'tres', 'quatro']

for box_name in boxes:
    div_number = find_by_text(box_name, browser, 'div')
    div_number.click()

for box_name in boxes:
    sleep(0.25)
    browser.back()

for box_name in boxes:
    sleep(0.25)
    browser.forward()
