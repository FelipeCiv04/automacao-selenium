from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.by import By
import random
from selenium.webdriver.support.select import Select

def iniciar_driver():
    chrome_options = Options()
    # Fonte de opções de switches https://peter.sh/experiments/chromium-command-line-switches/

    arguments = ['--lang=pt-BR', '--window-size=1200,700',
                '--incognito', '--disable-notifications']
    ''' Common arguments
    --start-maximized # Inicia maximizado
    --lang=pt-BR # Define o idioma de inicialização, # en-us , pt-BR
    --incognito # Usar o modo anônimo
    --window-size=800,800 # Define a resolução da janela em largura e altura
    --headless # Roda em segundo plano(com a janela fechada)
    --disable-notifications # Desabilita notificações
    --disable-gpu # Desabilita renderização com GPU
    '''
    for argument in arguments:
        chrome_options.add_argument(argument)

    caminho_padrao_para_download = 'D:\\seleniumdownloads'

    # Lista de opções experimentais(nem todas estão documentadas) https://chromium.googlesource.com/chromium/src/+/32352ad08ee673a4d43e8593ce988b224f6482d3/chrome/common/pref_names.cc
    chrome_options.add_experimental_option("prefs", {
        'download.default_directory': caminho_padrao_para_download,
        # Atualiza diretório para diretório passado acima
        'download.directory_upgrade': True,
        # Setar se o navegar deve pedir ou não para fazer download
        'download.prompt_for_download': False,
        "profile.default_content_setting_values.notifications": 2,  # Desabilita notificações
        # Permite realizar múltiplos downloads
        "profile.default_content_setting_values.automatic_downloads": 1,
    })

    driver = webdriver.Chrome(options=chrome_options)
    return driver

def digitar_letra_por_letra(element, text):
    for letra in text:
        element.send_keys(letra)
        sleep(random.randint(1,5)/30)

driver = iniciar_driver()
driver.get('https://cursoautomacao.netlify.app')
sleep(1)
aba_primaria = driver.current_window_handle
driver.execute_script("window.scrollTo(0,1000);")
sleep(2)
botao_aba = driver.find_element(By.XPATH, "//button[text() = 'Abrir aba']")
botao_aba.click()
sleep(3)
texto = "Eu, giorno giovanna tenho um sonho!"
abas = driver.window_handles
driver.switch_to.window(abas[1])
senha_input = driver.find_element(By.XPATH, "//input[@id = 'senha']")
digitar_letra_por_letra(senha_input, texto)
sleep(2)
driver.close()
sleep(2)
driver.switch_to.window(aba_primaria)
driver.execute_script("window.scrollTo(0, document.body.scrollTop)")
sleep(2)
input('')
driver.quit()