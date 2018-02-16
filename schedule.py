def parse_minutes(time_str):
    h, m = time_str[:-3].split(':')
    if(time_str[-2:] == "PM"):
        int(h) * 60 + int(m) + 720
    else:
        int(h) * 60 + int(m)


def parse_time(time_str, days):
    times = []
    dayInMinutes = 1440
    dayDict = {
            "M": 0,
            "T": dayInMinutes,
            "W": dayInMinutes * 2,
            "Th": dayInMinutes * 3,
            "F": dayInMinutes * 4,
            "S": dayInMinutes * 5,
            "U": dayInMinutes * 6}
    startTime, endTime = time_str.split('-')
    startTime = parse_minutes(startTime)
    endTime = parse_minutes(endTime)
    for day in days:
        times.insert({startTime+dayDict[day], endTime+dayDict[day]})
    return times


class Classie:
    def __init__(self, classObj):
        self.crn = classObj[0]['CRN']
        self.times = []
        for oneClass in classObj:
            tempTime = parse_time(oneClass['time'], oneClass['days'])
            for time in tempTime:
                self.times.insert(time)


#def doesItFit(class1, class2):



#def sort(schedule, otherClasses):




def main():
    classExample = [
        {
          "CRN": "40203", 
          "campus": "FH", 
          "course": "PHYS F004A01", 
          "days": "TTh", 
          "desc": "GENERAL PHYSICS (CALC)", 
          "end": "06/29/2018", 
          "instructor": "Cascarano", 
          "room": "4502", 
          "seats": "28", 
          "start": "04/09/2018", 
          "status": "Open", 
          "time": "10:00 AM-11:50 AM", 
          "units": "  6.00", 
          "wait_cap": "10", 
          "wait_seats": "10"
        }, 
        {
          "CRN": "40203", 
          "campus": "FH", 
          "course": "PHYS F004A01", 
          "days": "T", 
          "desc": "GENERAL PHYSICS (CALC)", 
          "end": "06/29/2018", 
          "instructor": "Low", 
          "room": "4715", 
          "seats": "28", 
          "start": "04/09/2018", 
          "status": "Open", 
          "time": "12:00 PM-02:50 PM", 
          "units": "  6.00", 
          "wait_cap": "10", 
          "wait_seats": "10"
        }, 
        {
          "CRN": "40203", 
          "campus": "FH", 
          "course": "PHYS F004A01", 
          "days": "F", 
          "desc": "GENERAL PHYSICS (CALC)", 
          "end": "06/29/2018", 
          "instructor": "Cascarano", 
          "room": "4502", 
          "seats": "28", 
          "start": "04/09/2018", 
          "status": "Open", 
          "time": "11:00 AM-11:50 AM", 
          "units": "  6.00", 
          "wait_cap": "10", 
          "wait_seats": "10"
        }
    ]
    print(Classie(classExample))


if __name__ == '__main__':
    main()
