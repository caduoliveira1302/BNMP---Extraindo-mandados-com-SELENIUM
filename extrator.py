from selenium import webdriver 
from selenium.webdriver.common.by import By
import os
import shutil
from time import sleep
import warnings
warnings.filterwarnings("ignore")


driver=webdriver.Chrome()

def get_url():
    '''
    Acessa a url do Portal BNMP
    '''
    url='https://portalbnmp.cnj.jus.br/#/pesquisa-peca' 
    driver=webdriver.Chrome()                           
    driver.get(url)


def state_input():
    '''
    Pesquisa mandados filtrando pelo Estado desejado
    '''
    select_state_btn=driver.find_element(by=By.XPATH, value='//*[@id="ui-fieldset-1-content"]/div/form/div[6]/div/p-dropdown/div/label')
    select_state_btn.click()

    state_name = str(input('Digite o nome do Estado: '))

    state_input=driver.find_element(by=By.XPATH, value='//*[@id="ui-fieldset-1-content"]/div/form/div[6]/div/p-dropdown/div/div[3]/div[1]/input')
    state_input.send_keys(state_name)

    state_input_click = driver.find_element(by=By.XPATH, value='/html/body/app-root/div/div/div[2]/div/app-pesquisa-peca/div[1]/p-fieldset/fieldset/div/div/form/div[6]/div/p-dropdown/div/div[3]/div[2]/ul/li')
    state_input_click.click()


def city_input():
    '''
    Pesquisa mandados filtrando por um município específico, caso desejado
    '''
    city_question = str(input('Deseja extrair mandados de algum município específico?  [S/N]: ')).upper()

    if city_question != 'S' or 'N':
        raise ValueError("""Digite 'S' para SIM ou 'N' para NÃO""")

    if city_question == 'S':
        city_name = str(input('Digite o nome do Município: '))
        city_box = driver.find_element(by=By.XPATH, value='//*[@id="ui-fieldset-1-content"]/div/form/div[7]/div/p-dropdown/div/label')
        city_box.click()
        city_input = driver.find_element(by=By.XPATH, value='//*[@id="ui-fieldset-1-content"]/div/form/div[7]/div/p-dropdown/div/div[3]/div[1]/input')
        city_input.send_keys(city_name)

        city_input_click = driver.find_element(by=By.XPATH, value='//*[@id="ui-fieldset-1-content"]/div/form/div[7]/div/p-dropdown/div/div[3]/div[2]/ul/li')
        city_input_click.click()
    else:
        pass


def search_download():
    '''
    Realiza a pesquisa e extrai o arquivo .csv dos mandados
    '''
    search_btn=driver.find_element(by=By.XPATH, value='//*[@id="ui-fieldset-1-content"]/div/form/div[14]/button[2]')
    search_btn.click()
    sleep(1.5)
    export_btn = driver.find_element(by=By.XPATH, value='/html/body/app-root/div/div/div[2]/div/app-pesquisa-peca/div[2]/app-botoes-exportacao/p-splitbutton/div/button[2]')
    export_btn.click()
    sleep(1.5)
    csv_btn = driver.find_element(by=By.XPATH, value='/html/body/app-root/div/div/div[2]/div/app-pesquisa-peca/div[2]/app-botoes-exportacao/p-splitbutton/div/div/ul/li[4]/a')
    csv_btn.click()


def move_dir():
    '''
    Move o arquivo .csv para o diretório do extrator .py
    '''
    source_dir = os.path.expanduser('~/Downloads')
    destination_dir = os.getcwd()

    for filename in os.listdir(source_dir):
        if filename.startswith('relatorio') and filename.endswith(".csv"):

            source_file = os.path.join(source_dir, filename)
            destination_file = os.path.join(destination_dir, filename)
            
            shutil.move(source_file, destination_file)
            print(f'{filename} foi movido para {destination_dir}')