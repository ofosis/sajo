import test2
def test1(userdata):
    data = test2.GetLuckyItem(userdata)
    data = test22()
    result = {
        'Num':data[0],
        'Direction':data[1],
        'Color': data[2],
        'Flavor': data[3],
        'Fruit': data[4],
        'Animal': data[5],
        'BodyParts': data[6],
        'Mind': data[7],
        'Guide': data[8],
        'NaverSummary': data[9],
        'NaverDetail': data[10]
    }
    return result
def test22():
    result=[]
    result.append(1)
    result.append("북쪽")
    result.append("검정계열")
    result.append("짠맛")
    result.append("과일")
    result.append("동물")
    result.append("심장")
    result.append("인자,사랑,인(仁)")
    result.append("오늘은 매사에 양보하고, 맘에 안 드는 사람이나 일이 있어도 화내지 마세요")
    result.append("11월 01일의 운세 총운은 “실천모드” 입니다.")
    result.append("겸손을 익혔을 때에 사람들은 당신에게 호감을 표시할 것입니다. 남을 배려하지 않고 당신만을 위해서 일했다면 그로 인해 얻는 것은 불리한 상황뿐일 것입니다. 조금은 당신이 생각하는 일을 진행함에 있어서 그날 하루의 전체적인 모습을 체크하는 것이 가장 중요합니다. 당신이 스스로 낮추고 노력하는 모습을 보이는 만큼 좋은 것은 없습니다. 그리고 당신 역시 혼자서 뭐든지 잘하던 때보다도 좀더 따스하고 즐겁고 느긋한, 행복한 분위기 속에서 즐겁게 하루를 마감할 수 있으니 염두에 두시기 바랍니다.")
    return result