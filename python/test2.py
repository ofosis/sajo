from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

def GetLuck(userdata):
    InitWebDriver()
    doTodayNaver(userdata)
    return GetLuckyItem(userdata)+TODOTest(userdata)
def InitWebDriver():
    global web, wait
    web = webdriver.Chrome()
    wait = WebDriverWait(web, 10)
def SendKeyByName(element_name, key_values):
    input_element = wait.until(EC.element_to_be_clickable((By.NAME, element_name)))
    input_element.send_keys(key_values)
    return
def GetTextBySelector(selector):
    element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,selector)))
    return element.text
def GetDataFromWeb():
    result=[]
    try:
        time.sleep(1)
        숫자 = GetTextBySelector('body > table:nth-child(2) > tbody > tr > td > table > tbody > tr:nth-child(1) > td:nth-child(2) > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td > table > tbody > tr:nth-child(4) > td > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(1) > td > b > font')
        숫자 = 숫자.split(":")[1].strip()
        숫자 = int(숫자)
        result.append(숫자)
        방향 = GetTextBySelector('body > table:nth-child(2) > tbody > tr > td > table > tbody > tr:nth-child(1) > td:nth-child(2) > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td > table > tbody > tr:nth-child(4) > td > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(2) > td > b > font')
        방향 = 방향.split(":")[1].strip()
        result.append(방향)
        색깔 = GetTextBySelector('body > table:nth-child(2) > tbody > tr > td > table > tbody > tr:nth-child(1) > td:nth-child(2) > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td > table > tbody > tr:nth-child(4) > td > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(3) > td > b > font')
        색깔 = 색깔.split(":")[1].strip()
        result.append(색깔)
        맛 = GetTextBySelector('body > table:nth-child(2) > tbody > tr > td > table > tbody > tr:nth-child(1) > td:nth-child(2) > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td > table > tbody > tr:nth-child(4) > td > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(4) > td > b > font')
        맛 = 맛.split(":")[1].strip()
        result.append(맛)
        과일 = GetTextBySelector('body > table:nth-child(2) > tbody > tr > td > table > tbody > tr:nth-child(1) > td:nth-child(2) > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td > table > tbody > tr:nth-child(4) > td > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(5) > td > b > font')
        과일 = 과일.split(":")[1].strip()
        result.append(과일)
        동물 = GetTextBySelector('body > table:nth-child(2) > tbody > tr > td > table > tbody > tr:nth-child(1) > td:nth-child(2) > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td > table > tbody > tr:nth-child(4) > td > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(6) > td > b > font')
        동물 = 동물.split(":")[1].strip()
        result.append(동물)
        신체부위 = GetTextBySelector('body > table:nth-child(2) > tbody > tr > td > table > tbody > tr:nth-child(1) > td:nth-child(2) > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td > table > tbody > tr:nth-child(4) > td > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td > table > tbody > tr > td > table > tbody > tr:nth-child(7) > td > b > font')
        result.append(신체부위)
        마음가짐 = GetTextBySelector('body > table:nth-child(2) > tbody > tr > td > table > tbody > tr:nth-child(1) > td:nth-child(2) > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td > table > tbody > tr:nth-child(4) > td > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td > table > tbody > tr > td > table > tbody > tr:nth-child(11) > td > b > font')
        result.append(마음가짐)
        생활가이드 = GetTextBySelector('body > table:nth-child(2) > tbody > tr > td > table > tbody > tr:nth-child(1) > td:nth-child(2) > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td > table > tbody > tr:nth-child(4) > td > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td > table > tbody > tr > td > table > tbody > tr:nth-child(15) > td > b > font')
        result.append(생활가이드)

        return result
    finally:
        web.quit()

def TranceTimeNum(time):
    valuedict = {
        0 : 99,
        1 : 0,
        2 : 2,
        3 : 4,
        4 : 6,
        5 : 8,
        6 : 10,
        7 : 12,
        8 : 14,
        9 : 16,
        10 : 18,
        11 : 20,
        12 : 22
    }
    return valuedict[time]

def GetLuckyItem(userdata):
    web.get('https://sazoo.com/ss/run/life/todayitem/')

    이름 = userdata['Name']
    SendKeyByName('mNA', 이름)

    년도 = userdata['BirthYear']
    SendKeyByName('mYY', 년도)

    월 = userdata['BirthMonth']
    if 월 != 1:
        SendKeyByName('mMM', 월)

    일 = userdata['BirthDay']
    if 일!=1:
        SendKeyByName('mDD', 일)

    시간 = TranceTimeNum(userdata['BirthTime'])
    SendKeyByName('mHH', 시간)

    성별 = '남성' if userdata['isMale'] else '여성'
    SendKeyByName('mSE', 성별)

    달력 = userdata['Calendar']
    SendKeyByName('mSL', 달력)

    time.sleep(3)
    web.execute_script("javascript:FormCheck()")

    result=GetDataFromWeb()

    return result

def TODOTest(userdata):
    result=[]
    네이버한줄 = '더미'
    result.append(네이버한줄)
    네이버상세 = '더미'
    result.append(네이버상세)
    return result

def ClickValueByName(key_values):
    target_value = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'ul[data-value="solar"]')))
    target_value.click()
    target_value = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'li[data-value="{key_values}"] a')))
    target_value.click()
    return
def SendValueById(element_id, key_values):
    input_element = wait.until(EC.element_to_be_clickable((By.ID, element_id)))
    input_element.send_keys(key_values)
    return
def ClickValueForGender(element_name, key_values):
    target_value = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'.{element_name}[for="{key_values}"]')))
    target_value.click()
    return
def doTodayNaver(userdata):
    web.get('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%98%A4%EB%8A%98%EC%9D%98+%EC%9A%B4%EC%84%B8')

    성별 = 'l_man' if userdata['isMale'] else 'l_woman'
    ClickValueForGender('_genderLabel',성별)

    생년월일=TranceBirthDay(userdata)
    SendValueById("srch_txt",생년월일)

    달력 = TranceCalendar(userdata['Calendar'])
    ClickValueByName(달력)

    시간 = TranceTimeNum(userdata['BirthTime'])


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
def TranceCalendar(calendar):
    valuedict = {
        '양력/평달' : "solar",
        '음력/평달' : "lunarGeneral",
        '음력/윤달' : "lunarLeap"
    }
    return valuedict[calendar]
def TranceBirthDay(userdata):
    년도 = userdata['BirthYear']
    월 = userdata['BirthMonth']
    일 = userdata['BirthDay']
    return f'{년도}{str(월).zfill(2)}{str(일).zfill(2)}'