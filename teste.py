from selenium import webdriver
from selenium.webdriver import Chrome

def video_youtube(url, nomeVideo):
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(1)
    busca = driver.find_element("id", 'search')
    busca.send_keys(nomeVideo)
    driver.implicitly_wait(1)
    botao_busca = driver.find_element("xpath", '//*[@id="search-icon-legacy"]')
    botao_busca.click()
    driver.implicitly_wait(1)
    inicio_video = driver.find_element("xpath", '//div[@class="text-wrapper style-scope ytd-video-renderer" and div[1]/div[1]/h3[1]/a]')
    inicio_video[0].click()
    WebDriverWait(driver, timeout=1000).util(driver.find_element("xpath", '//*[@id="ytp-id-18"]/div/div/div[4]/div[2]'))
    botao_detalhes = driver.find_element("xpath", '//*[@id="movie_player"]/div[29]/div[2]/div[2]/button[3]')
    botao_detalhes.click()
    driver.implicitly_wait(1)
    botao_qualidade = driver.find_element("xpath", '//*[@id="ytp-id-18"]/div/div/div[4]/div[2]')
    botao_qualidade.click()

    abaixar_qualidade_video = driver.find_element("xpath", )
    abaixar_qualidade_video.click()

video_youtube('https://www.youtube.com.br/', 'GATOS FOFOS E PERFEITOS!')