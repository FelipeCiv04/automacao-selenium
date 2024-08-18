from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import random 

def inicia_driver():
    chrome_options = Options()

    arguments = ['--lang=pt-BR', '--window-size=1200,700', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,

    })

    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)

    driver.get('https://cursoautomacao.netlify.app/')
    return driver
driver = inicia_driver()
def digital_naturalmente(texto, elemento):
    for letra in texto:
        elemento.send_keys(letra)
        sleep(random.randint(1,5)/30)
sleep(1)

driver.execute_script("window.scrollTo(0,400);")
paragrafo = driver.find_element(By.XPATH, "//textarea[@placeholder = 'digite seu texto aqui']")
sleep(2)
texto = """ Em uma manhã ensolarada de primavera, o parque da cidade estava cheio de vida. Crianças corriam e riam,
enquanto seus pais observavam atentamente, alguns segurando xícaras de café quentes. Perto do lago, um casal idoso alimentava os patos,
sorrindo nostalgicamente ao lembrar de tempos passados. Árvores florescendo em cores vibrantes criavam um cenário pitoresco,
e o ar fresco estava impregnado com o cheiro doce das flores. Mais adiante, um grupo de jovens praticava yoga,
buscando equilíbrio e tranquilidade em meio à natureza.
A cena inteira parecia uma pintura perfeita, um momento congelado no tempo,
repleto de simplicidade e beleza."""
digital_naturalmente(texto, paragrafo)
input('JSDFBJKHSDFKBJSDFJKHBSD')