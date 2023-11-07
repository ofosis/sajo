import time

from CrawlerController import *
from UserDataConverter import *
def TODOTest(userdata):
    result=[]
    네이버한줄 = '더미'
    result.append(네이버한줄)
    네이버상세 = '더미'
    result.append(네이버상세)
    return result

def doTodayNaver(userdata):
    web=InitWebDriver()
    web.get('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%98%A4%EB%8A%98%EC%9D%98+%EC%9A%B4%EC%84%B8')

    성별 = 'l_man' if userdata['isMale'] else 'l_woman'
    ClickValueForGender('_genderLabel',성별)

    생년월일=TranceBirthDay(userdata)
    SendValueById("srch_txt",생년월일)

    달력 = TranceCalendar(userdata['Calendar'])
    ClickValueByXPATH(web,1,달력)

    시간 = userdata['BirthTime']+1
    ClickValueByXPATH(web,2,시간)

    a=web.find_element(By.XPATH,'/html/body/div[3]/div[2]/div/div[1]/section[1]/div/div[2]/div[2]/div[1]/fieldset/input')
    a.click()

    result=GetDataFromWeb(web)
    return result


def GetDataFromWeb(web):
    result=[]
    try:
        한줄평=GetTextBySelector('#fortune_birthResult > dl.infor._luckText.v2 > dd > strong')
        result.append(한줄평)
        디테일=GetTextBySelector('#fortune_birthResult > dl.infor._luckText.v2 > dd > p')
        result.append(디테일)
        return result
    finally:
        web.quit()