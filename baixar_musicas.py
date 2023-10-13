from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import shutil
from datetime import datetime

# Mapeamento dos gêneros para suas respectivas páginas
generos_paginas = {
      # aqui dentro da lista põe a pagina web de onde vai baixar a musica, eu fiz para usar na musio mas pode usar a logica em qualquer pagina web
    'sertanejo': ["https://musio.net.br/henrique-juliano/","https://musio.net.br/leonardo/"],

    'pagode': [],

    'arrocha': [],

    'funk': [],

    'rap': []

}

# aqui é a pasta padrão onde são salvos os downloads no windowns , se a sua for outra lembre de mudar
pasta_downloads = os.path.expanduser('~') + '/Downloads/'

# Crie uma instância do navegador Edge
driver = webdriver.Edge()

try:
    # faço um laço em todas as paginas web escolhidas
    for genero, paginas in generos_paginas.items():
        for pagina in paginas:
            # Navegue até a página atual
            driver.get(pagina)

            # Encontre todos os botões "Baixar música" da pagina, aqui uso o botão de download da musio, se usar outra pagina web lembre de procurar qual o titulo do botão da pagina, só clicar f12 ou clica com o botão direito do mouse na pagina e vai em inspecionar depois em elementos e procura o botão
            download_buttons = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//button[@title='Baixar música']"))
            )

            # Itere sobre os botões e clique em cada um
            for button in download_buttons:
                

                # Use JavaScript para clicar no botão
                driver.execute_script("arguments[0].click();", button)
                print('')
                print(f'Download da {pagina} iniciado')
                print('')

                # Aguarde um tempo entre os downloads (por exemplo, 10 segundos)
                time.sleep(10)

            print(f'Todos os downloads de {genero} foram iniciados ')

            # Aguarde um tempo antes de mover os arquivos e navegar para a próxima página (por exemplo, 5 segundos)
            time.sleep(15)

            # Mova os arquivos para a pasta de destino correspondente ao gênero
            pasta_destino = f"C:/Users/igork/Desktop/automação de dados das musicas/musicas/{genero}"
            # Lista todos os arquivos na pasta de destino
            arquivos_destino = os.listdir(pasta_destino)

            #aqui faço um laço para mover os arquivos baixados de cada pagina para a pasta correta de acordo com a chave do dicionario, nesse caso as chaves são os generos musicais
            for filename in os.listdir(pasta_downloads):
                if filename.endswith('.mp3') and datetime.fromtimestamp(os.path.getctime(os.path.join(pasta_downloads, filename))).date() == datetime.today().date():
                    destino = os.path.join(pasta_destino, filename)
# aqui faço uma verificação  se o arquivo ja foi baixado e se ja foi ele é excluido para não haver duplicidade
                    if filename in arquivos_destino:
                        os.remove(destino)
                    # depois de tudo verificado todos os arquivos são movidos para a pasta correta 
                    shutil.move(os.path.join(pasta_downloads, filename), pasta_destino)

            print(f'Todos os arquivos de {genero} foram movidos para a pasta de destino.')

    # Encerre o navegador quando todas as páginas forem processadas
    driver.quit()

# aqui é só se der alguem erro, ai vai mostrar o erro no terminal
except Exception as e:
    print(f" Deu Erro mané: {e}")

print('Todos os arquivos foram baixados e movidos para as pastas de destino correspondentes.')
