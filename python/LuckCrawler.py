from GetDataWithsaju import GetLuckyItem
from GetDataWithNaver import doTodayNaver
def TranceLuckData(userdata):
    data = GetLuck(userdata)
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
def GetLuck(userdata):
    return GetLuckyItem(userdata)+doTodayNaver(userdata)