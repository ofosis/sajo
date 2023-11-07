#사주닷컴
def TranceTimeNum(time):
    valuedicttime = {
        '99' : 99,
        '0' : 1,
        '2' : 1,
        '4' : 2,
        '6' : 3,
        '8' : 4,
        '10' : 5,
        '12' : 1,
        '14' : 2,
        '16' : 3,
        '18' : 4,
        '20' : 5,
        '22' : 2
    }
    valuedict = {
        '99': 99,
        '0': 2,
        '2': 0,
        '4': 0,
        '6': 0,
        '8': 0,
        '10': 0,
        '12': 1,
        '14': 1,
        '16': 1,
        '18': 1,
        '20': 1,
        '22': 2
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
        '0' : 2,
        '2' : 3,
        '4' : 4,
        '6' : 5,
        '8' : 6,
        '10' : 7,
        '12' : 8,
        '14' : 9,
        '16' : 10,
        '18' : 11,
        '20' : 12,
        '22' : 13
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