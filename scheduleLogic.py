def isOverLapping(classArr, class2):
    newSchedule = class2.times
    for section in classArr:
        newSchedule += section.times
    newSchedule = sorted(newSchedule, key=lambda x: x[0])
    print(newSchedule)
    for i in range(1, len(newSchedule) - 1):
        if(newSchedule[i-1][1] > newSchedule[i][0]):
            return True
        return False


def findPossibleSchedule(schedule, otherClasses, possibleSchedlues):
    if len(otherClasses) <= 0:
        possibleSchedlues.append(schedule)
        return True
    for section in otherClasses[0]:
        condition = isOverLapping(schedule, section)
        if not condition:
            return findPossibleSchedule(schedule+section, otherClasses.pop(0))
        else:
            return False

def schedulize(coursesArray):
    possibleSchedules = []
    sectionArray = []
    coursesArray = sorted(coursesArray, key=len)
    print(coursesArray)
    for course in coursesArray:
        sectionArray.append(course)
    for section in sectionArray[0]:
        findPossibleSchedule(section, sectionArray[1:], possibleSchedules)
    print(possibleSchedules)

