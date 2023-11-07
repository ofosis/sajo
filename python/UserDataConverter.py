def TranceTimeNum(time):
    valuedicttime = {
        0 : 99,
        1 : 1,
        2 : 1,
        3 : 2,
        4 : 3,
        5 : 4,
        6 : 5,
        7 : 1,
        8 : 2,
        9 : 3,
        10 : 4,
        11 : 5,
        12 : 2
    }
    valuedict = {
        0: 99,
        1: 2,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 1,
        8: 1,
        9: 1,
        10: 1,
        11: 1,
        12: 2
    }
    return valuedict[time],valuedicttime[time]

def TranceCalendar(calendar):
    valuedict = {
        '양력/평달' : "/li[1]",
        '음력/평달' : "/li[2]",
        '음력/윤달' : "/li[3]"
    }
    return valuedict[calendar]

def TranceBirthDay(userdata):
    년도 = userdata['BirthYear']
    월 = userdata['BirthMonth']
    일 = userdata['BirthDay']
    return f'{년도}{str(월).zfill(2)}{str(일).zfill(2)}'