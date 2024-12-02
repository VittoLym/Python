from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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

input_element_pswd.send_keys(Keys.RETURN)

WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.ID, 'portletComponentApplications_menuActionNormalModeApplications__id185_4_applicationLink'))
)

Input_consult = driver.find_element(By.ID, 'portletComponentApplications_menuActionNormalModeApplications__id185_4_applicationLink')
Input_consult.click()

driver.switch_to.frame("executionPanelApplications")
input_tel = WebDriverWait(driver, 15).until(
    EC.visibility_of_element_located((By.ID, 'att\\$nroLinea'))
)
input_tel.send_keys('3412003165')


WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.ID, 'att\\$button6'))
)

input_search_consult = driver.find_element(By.ID, 'att$button6')
input_search_consult.click()

WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.ID, 'array1_5_header'))
)

input_date = driver.find_element(By.ID, 'grp\\$array1\\$detalle$0')
input_date.click()

WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.ID, 'operador_comp'))
)
number_opi = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.ID, 'nroLineaCombo_comp'))
)

opi = driver.find_element(By.ID, 'operador_comp')

print(f'{opi.text}&&{number_opi.text}')

time.sleep(5)

driver.quit()