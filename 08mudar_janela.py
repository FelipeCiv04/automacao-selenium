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
janela_inicial = driver.current_window_handle
print(f'a janela atual é {janela_inicial}')
driver.execute_script("window.scrollTo(0,650 );")
botao = driver.find_element(By.XPATH, "//button[text()='Abrir Janela']")
sleep(0.5)
botao.click()
#driver.execute_script('arguments[0].click()', botao)
#Se o .click() nao funfar, usar esse
sleep(2)
janelas = driver.window_handles
for janela in janelas:
    print(janela)
    #se a janela atual nao for a janela inicial
    if janela not in janela_inicial:
        #alterar para essa nova janela
        driver.switch_to.window(janela)
        sleep(1)
        botao_pesquisa = driver.find_element(By.XPATH, "//button[@id='fazer_pesquisa']")
        sleep(0.5)
        campo_pesquisa = driver.find_element(By.XPATH, "//input[@id = 'campo_pesquisa']")
        sleep(0.5)
        texto_pesquisa = ('Obras de Arte mais caras do mundo atualmente')
        digitar_letra_por_letra(campo_pesquisa, texto_pesquisa)
        botao_pesquisa.click()
        sleep(2)
        driver.close()
driver.switch_to.window(janela_inicial)


input('')
driver.quit()
