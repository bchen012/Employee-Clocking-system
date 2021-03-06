import datetime

weekDays = ("M","T","W","T","F","S","S")

# += datetime.timedelta(days=1)
def get_weekDay(date):
    return weekDays[date.weekday()]


def format_date(date):
    return date.strftime("%d/%m/%y")


def get_time_difference(time1, time2):
    h1 = int(time1[:2])
    h2 = int(time2[:2])
    m1 = int(time1[2:])
    m2 = int(time2[2:])
    diff = (h2-h1)*4
    diff += (m2-m1)//15
    return diff


def print_Attendance(attendanceList):
    print("Date    |Day|0800|0900|1000|1100|1200|1300|1400|1500|1600|1700|1800|1900|2000|2100|2200|2300|")
    dates = []
    times = []
    for i in attendanceList:
        dateTime = i.split(' ')
        dateData = dateTime[0].split('/')
        date = datetime.date(int(dateData[2]), int(dateData[1]), int(dateData[0]))
        dates.append(date)
        times.append(dateTime[1])
    
    i = 0
    clockedIn = False
    clockInTime = '0000'
    PrevClockOutTime = '0800'

    while i < len(dates):
        currentDate = dates[i]
        print(format_date(currentDate) + "|" + get_weekDay(currentDate), end="  ")
        scheduleToPrint = ""
        while i < len(dates) and currentDate == dates[i]:
            time = times[i]
            if not clockedIn:
                clockInTime = time
                clockedIn = True
            else:
                clockedIn = False
                sinceLastClockIn = get_time_difference(PrevClockOutTime, clockInTime)
                for j in range(sinceLastClockIn):
                    if len(scheduleToPrint)>=4:
                        scheduleToPrint += 'X'      #print late indicator
                    else:
                        scheduleToPrint += ' '

                workDuration = get_time_difference(clockInTime, time)
                for j in range(workDuration):
                    if len(scheduleToPrint) >= 40:
                        scheduleToPrint += 'T'
                    else:
                        scheduleToPrint += 'O'
                
                PrevClockOutTime = time
                
            i+=1
        for j in range(len(scheduleToPrint), 64):
            scheduleToPrint += ' '
        index = 0
        for j in scheduleToPrint:
            if index%4 == 0:
                print('|', end='')
            print(j, end='')
            index += 1
        PrevClockOutTime = '0800'
        print("|")

    print('')
    print("Legend: \nO - Clocked in \nX - Late \nT - Overtime \n\n")
