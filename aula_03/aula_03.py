from selenium.webdriver import Firefox
from time import sleep

browser = Firefox()

url = 'https://curso-python-selenium.netlify.app/aula_03.html'

browser.get(url)

sleep(1)

a = browser.find_element_by_tag_name('a')
p = browser.find_element_by_tag_name('p')


print(f'texto de a: {a.text}')
print(f'texto de p: {p.text}')

for i in range(10):
    a.click()

ps = browser.find_elements_by_tag_name('p')


for n, i in enumerate(ps):
    print(f'texto de p[{n}]: {i.text}')

browser.quit()