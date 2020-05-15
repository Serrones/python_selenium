from selenium.webdriver import Firefox
from urllib.parse import urlparse


url = 'https://selenium.dunossauro.live/aula_04_a.html'

browser = Firefox()

browser.get(url)

split_url = urlparse(browser.current_url)

print(split_url)

print(split_url.scheme)

print(split_url.netloc)

print(split_url.path)

browser.refresh()

print(browser.title)
