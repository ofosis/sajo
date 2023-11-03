
from CrawlController import *
from UserDataConverter import *
def doTodayNaver(userdata):
    web.get('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%98%A4%EB%8A%98%EC%9D%98+%EC%9A%B4%EC%84%B8')

    성별 = 'l_man' if userdata['isMale'] else 'l_woman'
    ClickValueForGender('_genderLabel',성별)

    생년월일=TranceBirthDay(userdata)
    SendValueById("srch_txt",생년월일)

    달력 = TranceCalendar(userdata['Calendar'])
    ClickValueByName(달력)

    시간 = TranceTimeNum(userdata['BirthTime'])

    web.execute_script('result_solo()')

    try:
        element = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".today_f_tit"))
        )
        div = web.find_element(By.CSS_SELECTOR,'.today_f_txt')
        print(div.text)
        return div.text
    finally:
        web.quit()

#더미데이터
def TODOTest(userdata):
    result=[]
    네이버한줄 = '더미'
    result.append(네이버한줄)
    네이버상세 = '더미'
    result.append(네이버상세)
    return result