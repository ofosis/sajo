import time

from CrawlerController import *
from UserDataConverter import *

def doTodayNaver(userdata):
    web=InitWebDriver()
    web.get('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%98%A4%EB%8A%98%EC%9D%98+%EC%9A%B4%EC%84%B8')

    xpath='/html/body/div[3]/div[2]/div/div[1]/section[1]/div/div[2]/div[2]/div[1]/fieldset/'

    성별 = 'div[1]/label[1]' if userdata['isMale']=='0' else 'div[1]/label[2]'
    ClickValueForGender(xpath+성별)

    생년월일=TranceBirthDay(userdata)
    SendValueByXPATH(xpath+'div[2]/input',생년월일)

    달력 = TranceCalendarNaver(userdata['Calendar'])
    ClickValueByXPATH(web,xpath+'div[3]/ul[1]',달력)

    시간 = f"/li[{TranceTimeNumNaver(userdata['BirthTime'])}]"
    ClickValueByXPATH(web,xpath+'div[3]/ul[2]',시간)

    a=web.find_element(By.XPATH,'/html/body/div[3]/div[2]/div/div[1]/section[1]/div/div[2]/div[2]/div[1]/fieldset/input')
    a.click()

    result=GetDataFromWeb(web)
    return result


def GetDataFromWeb(web):
    result=[]
    try:
        xpath='/html/body/div[3]/div[2]/div/div[1]/section[1]/div/div[2]/div[2]/div[2]/dl[1]/dd/'
        한줄평=GetTextBySelector(xpath+'strong')
        result.append(한줄평)
        디테일=GetTextBySelector(xpath+'p')
        result.append(디테일)
        return result
    finally:
        web.quit()