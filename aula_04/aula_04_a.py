from selenium.webdriver import Firefox

url = 'https://selenium.dunossauro.live/aula_04_a.html'

browser = Firefox()

browser.get(url)

lista_nao_ordenada = browser.find_element_by_tag_name('ul') # 1

lista_lis = lista_nao_ordenada.find_elements_by_tag_name('li') # 2

nome_ancora = lista_lis[0].find_element_by_tag_name('a').text # 3

ancora = lista_lis[0].find_element_by_tag_name('a') # 4

href = ancora.get_attribute('href') # 5


"""
1 - Buscamos o primeiro ul

2 - Pegamos todos os li dentro do primeiro ul

3 - Pegamos o texto dentro do primeiro li (que é o text da âncora)

4 - Pegamos a âncora dentro do primeiro li

5 - Pegamos o href da âncora

ul
    li
        a
            text
    li
        a
            text
"""