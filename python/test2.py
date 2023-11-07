from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def SendKeyByName(element_name, key_values):
    input_element = wait.until(EC.element_to_be_clickable((By.NAME, element_name)))
    input_element.send_keys(key_values)
    return
def GetLuckyItem(userdata):
    global web, wait
    web = webdriver.Chrome()
    web.get('https://sazoo.com/ss/run/life/todayitem/')
    wait = WebDriverWait(web, 10)

    이름=userdata['Name']
    SendKeyByName('mNA',이름)

    년도=userdata['BirthYear']
    SendKeyByName('mYY', 년도)

    월=userdata['BirthMonth']
    SendKeyByName('mMM', 월)

    일=userdata['BirthDay']
    SendKeyByName('mDD', 일)

    시간=userdata['BirthTime']
    SendKeyByName('mHH', 시간)

    성별='남성' if userdata['isMale'] else '여성'
    SendKeyByName('mSE', 성별)

    달력=userdata['Calendar']
    SendKeyByName('mSL', 달력)

    web.execute_script("javascript:FormCheck()")
    time.sleep(5)
    print(7)
    return "안녕"
    try:
        element = WebDriverWait(web, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".saju_box"))
        )
        div = web.find_element(By.CSS_SELECTOR,'#content > article > div.result > div.saju_box > div:nth-child(6)')
        return div.text
    finally:
        time.sleep(5)
        web.quit()

def doToday():
    web = webdriver.Chrome()
    web.get('https://m.unsin.co.kr/unse/free/today/form')

    이름 = web.find_element(By.CSS_SELECTOR, '#user_name')
    이름.send_keys('abcd')

    년도 = web.find_element(By.CSS_SELECTOR, '#birth_yyyy')
    년도.send_keys('1985년')

    월 = web.find_element(By.CSS_SELECTOR, '#birth_mm')
    월.send_keys('5월')

    일자 = web.find_element(By.CSS_SELECTOR, '#birth_dd')
    일자.send_keys('11일')

    시간 = web.find_element(By.CSS_SELECTOR, '#birth_hh')
    시간.send_keys('申 (15:30 ~ 17:29)')

    양력음력 = web.find_element(By.CSS_SELECTOR, '#birth_solunar')
    양력음력.send_keys('양력')

    time.sleep(3)
    web.execute_script('result_solo()')
    time.sleep(5)

    try:
        element = WebDriverWait(web, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".today_f_tit"))
        )
        div = web.find_element(By.CSS_SELECTOR,'.today_f_txt')
        print(div.text)
        return div.text
    finally:
        time.sleep(5)
        web.quit()
