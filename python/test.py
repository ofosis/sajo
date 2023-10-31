import sys

# 파이썬 스크립트로부터 데이터 읽기
data = sys.stdin.read().strip()

# 데이터를 분리하여 리스트로 저장 (줄바꿈 문자를 구분자로 사용)
data_list = data.split('\n')

# 데이터 처리 예시:
name, year,month,day, time, gender, calendar = data_list
name="성명:"+name
birth="생년월일:"+year+"년"+month+"월"+day+"일"
time="시간:"+time
gender="성별:"+gender
calendar="사용달력:"+ calendar
processed_data=name,birth,time,gender,calendar
result=("1",
        "북쪽",
        "검정계열",
        "짠맛",
        "과일",
        "동물",
        "심장",
        "인자,사랑,인(仁)",
        "오늘은 매사에 양보하고, 맘에 안 드는 사람이나 일이 있어도 화내지 마세요")

# 처리된 데이터를 C#에게 반환
response = '\n'.join(result)
print(response)
sys.stdout.flush()