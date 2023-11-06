from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

def Setting():
    web = webdriver.Chrome()
    wait = WebDriverWait(web, 10)
    return web,wait

#사주닷컴 컨트롤러
def SendKeyByName(wait,element_name, key_values):
    input_element = wait.until(EC.element_to_be_clickable((By.NAME, element_name)))
    input_element.send_keys(key_values)
    return
def GetTextBySelector(wait,selector):
    element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,selector)))
    return element.text
#네이버용 컨트롤러
def ClickValueByName(wait,key_values):
    target_value = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'ul[data-value="solar"]')))
    target_value.click()
    target_value = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'li[data-value="{key_values}"] a')))
    target_value.click()
    return
def SendValueById(wait,element_id, key_values):
    input_element = wait.until(EC.element_to_be_clickable((By.ID, element_id)))
    input_element.send_keys(key_values)
    return
def ClickValueForGender(wait,element_name, key_values):
    target_value = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'.{element_name}[for="{key_values}"]')))
    target_value.click()
    return