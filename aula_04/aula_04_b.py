from selenium.webdriver import Firefox

def find_by_text(text, browser, tag):
    """
    Encontrar o elemento com o texto passado como argumento

    Argumentos
    text - conteúdo que deve estar na tag
    browser - instância do selenium 
    tag - tag onde o texto será procurado 
    """
    tag_list = browser.find_elements_by_tag_name(tag)

    for item in tag_list:
        if item.text == text:
            return item

def find_by_href(link, browser):
    """
    Encontrar elemento pelo href
    
    Argumentos
    link - link que será procurado em todas as tags 'a'
    browser - instância do selenium
    
    """
    anchor_list = browser.find_elements_by_tag_name('a')

    for item in anchor_list:
        if link in item.get_attribute('href'):
            return item


if __name__ == '__main__':
    url = 'https://selenium.dunossauro.live/aula_04_a.html'

    browser = Firefox()

    browser.get(url)

    ddg = find_by_text('DuckDuckGo', browser, 'li')

    ggl = find_by_href('google', browser)