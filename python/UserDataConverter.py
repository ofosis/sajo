#사주닷컴
def TranceTimeNum(time):
    valuedict = {
        '99': 99,
        '1': 2,
        '2': 0,
        '3': 0,
        '4': 0,
        '5': 0,
        '6': 0,
        '7': 1,
        '8': 1,
        '9': 1,
        '10': 1,
        '11': 1,
        '12': 2
    }
    valuedicttime = {
        '99' : 99,
        '1' : 1,
        '2' : 1,
        '3' : 2,
        '4' : 3,
        '5' : 4,
        '6' : 5,
        '7' : 1,
        '8' : 2,
        '9' : 3,
        '10' : 4,
        '11' : 5,
        '12' : 2
    }
    return valuedict[time],valuedicttime[time]

def TranceCalendarSaju(calendar):
    valuedict = {
        '0' : '양력/평달',
        '1' : '음력/평달',
        '2' : '음력/윤달'
    }
    return valuedict[calendar]
#네이버
def TranceTimeNumNaver(time):
    valuedict = {
        '99' : 1,
        '1' : 2,
        '2' : 3,
        '3' : 4,
        '4' : 5,
        '5' : 6,
        '6' : 7,
        '7' : 8,
        '8' : 9,
        '9' : 10,
        '10' : 11,
        '11' : 12,
        '12' : 13
    }
    return valuedict[time]

def TranceCalendarNaver(calendar):
    valuedict = {
        '0' : "/li[1]",
        '1' : "/li[2]",
        '2' : "/li[3]"
    }
    return valuedict[calendar]

def TranceBirthDay(userdata):
    년도 = userdata['BirthYear']
    월 = userdata['BirthMonth']
    일 = userdata['BirthDay']
    return f'{년도}{str(월).zfill(2)}{str(일).zfill(2)}'