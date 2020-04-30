"""
Crie um programa com selenium que
- gere um dicionário, onde a chave é a tag H1
- o valor deve ser um novo dicionário
- cada chave do valor deverá ser o valor do atributo
- cada valor deve ser o texto contido no elemento
"""
from selenium.webdriver import Firefox
from time import sleep

browser = Firefox()

url = 'https://curso-python-selenium.netlify.app/exercicio_01.html'

browser.get(url)

sleep(1)

element_dict = dict()

h1 = browser.find_element_by_tag_name('h1')
element_dict['h1'] = h1.text
element_dict['atributos'] = dict()

ps = browser.find_elements_by_tag_name('p')

for item in ps:
    element_dict['atributos'][item.get_attribute('atributo')] = item.text

print(element_dict)

browser.quit()
