import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

def InitWebDriver():
    global wait
    web = webdriver.Chrome()
    wait = WebDriverWait(web, 5)
    return web
#사주닷컴
def SendKeyByName(element_name, key_values):
    input_element = wait.until(EC.element_to_be_clickable((By.XPATH, element_name)))
    input_element.send_keys(key_values)
    return
def SendKeyBy(element_name, key_values,time):
    input_element = wait.until(EC.element_to_be_clickable((By.XPATH, element_name)))
    for _ in range(time):
        input_element.send_keys(key_values)
    return
def GetTextBySelector(xpath):
    element = wait.until(EC.element_to_be_clickable((By.XPATH,xpath)))
    return element.text

#네이버
def ClickValueByXPATH(web,xpath,key_values):
    web.find_element(By.XPATH,xpath).click()
    xpath_key_values=f'{xpath}{key_values}'
    web.find_element(By.XPATH,xpath_key_values).click()
    return
def SendValueByXPATH(xpath, key_values):
    input_element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
    input_element.send_keys(key_values)
    return
def ClickValueForGender(xpath):
    target_value = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
    target_value.click()
    return