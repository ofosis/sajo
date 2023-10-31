import sys

# 파이썬 스크립트로부터 데이터 읽기
data = sys.stdin.read().strip()

# 데이터를 분리하여 리스트로 저장 (줄바꿈 문자를 구분자로 사용)
data_list = data.split('\n')

# 데이터 처리 예시:
name, birth, time, gender, calendar = data_list
name="성명:"+name
birth="생년월일:"+birth
time="시간:"+time
gender="성별:"+gender
calendar="사용달력:"+ calendar
processed_data=name,birth,time,gender,calendar

# 처리된 데이터를 C#에게 반환
response = '\n'.join(processed_data)
print(response)
sys.stdout.flush()