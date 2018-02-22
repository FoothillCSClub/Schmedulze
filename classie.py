def parse_minutes(time_str):
    h, m = time_str[:-3].split(':')
    if(time_str[-2:] == "PM"):
        return int(h) * 60 + int(m) + 720
    else:
        return int(h) * 60 + int(m)


def parse_time(time_str, days):
    times = []
    dayInMinutes = 1440
    dayDict = {
            "M": 0,
            "T": dayInMinutes,
            "W": dayInMinutes * 2,
            "R": dayInMinutes * 3,
            "Th": dayInMinutes * 3,
            "F": dayInMinutes * 4,
            "S": dayInMinutes * 5,
            "U": dayInMinutes * 6}
    startTime, endTime = time_str.split('-')
    startTime = parse_minutes(startTime)
    endTime = parse_minutes(endTime)
    if days.find("Th") == 1:
        addDayMin = int(dayDict["Th"])
        times.append((startTime+addDayMin, endTime+addDayMin))
        days = days.replace("Th", "")
    for day in days:
        addDayMin = int(dayDict[day])
        times.append((startTime+addDayMin, endTime+addDayMin))
    return times


class Section:
    def __init__(self, classObj):
        self.crn = classObj[0]['CRN']
        self.times = []
        for oneClass in classObj:
            tempTime = parse_time(oneClass['time'], oneClass['days'])
            for time in tempTime:
                self.times.append(time)


