import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def InitWebDriver():
    global wait
    web = webdriver.Chrome()
    wait = WebDriverWait(web, 5)
    return web
#사주닷컴
def SendKeyByName(element_name, key_values):
    input_element = wait.until(EC.element_to_be_clickable((By.NAME, element_name)))
    input_element.send_keys(key_values)
    return
def GetTextBySelector(selector):
    element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,selector)))
    return element.text
#네이버
def ClickValueByXPATH(web,xpath,key_values):
    web.find_element(By.XPATH,
                     f'/html/body/div[3]/div[2]/div/div[1]/section[1]/div/div[2]/div[2]/div[1]/fieldset/div[3]/ul[{xpath}]').click()
    web.find_element(By.XPATH,
                     f'/html/body/div[3]/div[2]/div/div[1]/section[1]/div/div[2]/div[2]/div[1]/fieldset/div[3]/ul[{xpath}]/li[{key_values}]').click()
    return
def SendValueById(element_id, key_values):
    input_element = wait.until(EC.element_to_be_clickable((By.ID, element_id)))
    input_element.send_keys(key_values)
    return
def ClickValueForGender(element_name, key_values):
    target_value = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'.{element_name}[for="{key_values}"]')))
    target_value.click()
    return