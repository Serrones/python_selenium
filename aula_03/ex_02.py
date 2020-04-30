"""
Você tem um "número esperado",
e deve clicar em "clique aqui" até
o resultado ser igual ao número esperado
"""
from selenium.webdriver import Firefox
from time import sleep

browser = Firefox()

url = 'https://curso-python-selenium.netlify.app/exercicio_02.html'

browser.get(url)

sleep(1)

ps = browser.find_elements_by_tag_name('p')
num_esperado = ps[-1].text[-1]

a = browser.find_element_by_tag_name('a')

count = 0
while True:
    a.click()
    count += 1
    num_clicks = browser.find_elements_by_tag_name('p')
    num = num_clicks[-1].text[-1]
    if num == num_esperado:
        print(f'você ganhou na tentativa {count}')
        break

browser.quit()