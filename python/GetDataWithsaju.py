import time

from CrawlerController import *
from UserDataConverter import *

def GetLuckyItem(userdata):
    web=InitWebDriver()
    web.get('https://sazoo.com/ss/run/life/todayitem/')

    xpath='/html/body/table[2]/tbody/tr/td/table/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/'

    이름 = userdata['Name']
    SendKeyByName(xpath+'tr[1]/td/table/tbody/tr/td[2]/input', 이름)

    년도 = userdata['BirthYear']
    SendKeyByName(xpath+'tr[2]/td/table/tbody/tr/td[2]/input', 년도)

    월 = userdata['BirthMonth']
    if 월 != 1:
        SendKeyByName(xpath+'tr[2]/td/table/tbody/tr/td[2]/select[1]', 월)

    일 = userdata['BirthDay']
    if 일!=1:
        SendKeyByName(xpath+'tr[2]/td/table/tbody/tr/td[2]/select[2]', 일)

    시간,횟수 = TranceTimeNum(userdata['BirthTime'])
    SendKeyBy(xpath+'tr[2]/td/table/tbody/tr/td[2]/select[3]', 시간,횟수)

    성별 = '남성' if userdata['isMale']=='0' else '여성'
    SendKeyByName(xpath+'tr[3]/td/table/tbody/tr/td[1]/table/tbody/tr/td[2]/select', 성별)

    달력 = TranceCalendarSaju(userdata['Calendar'])
    SendKeyByName(xpath+'tr[3]/td/table/tbody/tr/td[3]/table/tbody/tr/td[2]/select', 달력)

    web.execute_script("javascript:FormCheck()")

    result=GetDataFromWeb(web)

    return result
def GetDataFromWeb(web):
    result=[]
    try:
        xpath='/html/body/table[2]/tbody/tr/td/table/tbody/tr[1]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[4]/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/'
        숫자 = GetTextBySelector(xpath+'tr[3]/td/table/tbody/tr[1]/td/b')
        숫자 = 숫자.split(":")[1].strip()
        숫자 = int(숫자)
        result.append(숫자)
        방향 = GetTextBySelector(xpath+'tr[3]/td/table/tbody/tr[2]/td/b')
        방향 = 방향.split(":")[1].strip()
        result.append(방향)
        색깔 = GetTextBySelector(xpath+'tr[3]/td/table/tbody/tr[3]/td/b')
        색깔 = 색깔.split(":")[1].strip()
        result.append(색깔)
        맛 = GetTextBySelector(xpath+'tr[3]/td/table/tbody/tr[4]/td/b')
        맛 = 맛.split(":")[1].strip()
        result.append(맛)
        과일 = GetTextBySelector(xpath+'tr[3]/td/table/tbody/tr[5]/td/b')
        과일 = 과일.split(":")[1].strip()
        result.append(과일)
        동물 = GetTextBySelector(xpath+'tr[3]/td/table/tbody/tr[6]/td/b')
        동물 = 동물.split(":")[1].strip()
        result.append(동물)
        신체부위 = GetTextBySelector(xpath+'tr[7]/td/b')
        result.append(신체부위)
        마음가짐 = GetTextBySelector(xpath+'tr[11]/td/b')
        result.append(마음가짐)
        생활가이드 = GetTextBySelector(xpath+'tr[15]/td/b')
        result.append(생활가이드)

        return result
    finally:
        web.quit()