from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="./geckodriver.exe")

driver = webdriver.Firefox(service=service)

driver.get('http://iris.tmoviles.com.ar/workspace/faces/jsf/workspace/workspace.xhtml')

input_element_mail = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "loginForm:workspace_login_user_name"))
)
input_element_mail.send_keys("faquirog")

input_element_pswd = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "loginForm:workspace_login_password"))
)
input_element_pswd.send_keys("nodar2022+")

input_element_pswd.submit()


WebDriverWait(driver, 15).until(
    EC.presence_of_all_elements_located((By.ID, 'portletComponentApplications_menuActionNormalModeApplications__id185_4_applicationLink'))
)

Input_consult = driver.find.element(By.ID, 'portletComponentApplications_menuActionNormalModeApplications__id185_4_applicationLink')
Input_consult.click()


WebDriverWait(driver, 15).until(
    EC.presence_of_all_elements_located((By.ID, 'label54_text'))
)

input_tel = driver.find_element(By.ID, 'label54_text')
input_tel.send_keys('3412003165')

WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.ID, 'att$button6'))
)

input_search_consult = driver.find_element(By.ID, 'att$button6')
input_search_consult.click()

WebDriverWait(driver, 15).until(
    EC.presence_of_all_elements_located((By.ID, 'array1_5_header'))
)

input_date = driver.find_element(By.ID, 'array1_5_header')
input_date.click()

WebDriverWait(driver, 15).until(
    EC.presence_of_all_elements_located((By.ID, 'operador_comp'))
)
opi = driver.find_element(By.ID, 'operador_comp')

print(f'{opi}')

time.sleep(5)
