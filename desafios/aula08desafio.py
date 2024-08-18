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
driver.get('https://cursoautomacao.netlify.app/desafios')
sleep(1)
janela_inicial = driver.current_window_handle
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
campo_final_da_tela = driver.find_element(By.XPATH, "//textarea[@id = 'campo_desafio7']")
sleep(5)
window_button = driver.find_element(By.XPATH,"//button[text() = 'Abrir nova janela']")
sleep(1)
window_button.click()
sleep(1)
text = 'Texto automatizado usando Python e Selenium'
janelas = driver.window_handles
for janela in janelas:
    if janela not in janela_inicial:
        driver.switch_to.window(janela)
        areadetexto = driver.find_element(By.XPATH, "//textarea[@class = 'form-control']")
        sleep(1)
        digitar_letra_por_letra(areadetexto, text)
        sleep(1)
        botao_pesquisa = driver.find_element(By.XPATH, "//button[@class = 'btn btn-success']")
        botao_pesquisa.click()
        driver.close
driver.switch_to.window(janela_inicial)
digitar_letra_por_letra(campo_final_da_tela, text)
    
input('')
driver.quit