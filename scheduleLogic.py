import sectionClass


def isOverLapping(classArr, classArr2):
    newSchedule = []
    for section in classArr:
        newSchedule += section.time
    for section in classArr2:
        newSchedule += section.time
    newSchedule = sorted(newSchedule, key=lambda x: x[0])
    print(newSchedule)
    for i in range(1, len(newSchedule) - 1):
        if(newSchedule[i-1][1] > newSchedule[i][0]):
            return True
        return False


def findPossibleSchedule(schedule, otherClasses, possibleSchedules):
    if len(otherClasses) <= 0:
        possibleSchedules.append(schedule)
        return True
    print(schedule, "\n\n", otherClasses[0])
    condition = isOverLapping([schedule], otherClasses[0])
    if not condition:
        return findPossibleSchedule(schedule + otherClasses[0],
                otherClasses.pop(0))
    else:
        return False


def schedulize(parsedCoursesArray):
    print(parsedCoursesArray)
    possibleSchedules = []
    print("Parsed Array:", parsedCoursesArray, "\n\n\n\n")
    for section in parsedCoursesArray[0]:
        findPossibleSchedule(section, parsedCoursesArray[1:],
                possibleSchedules)
    for section in possibleSchedules:
        print(section, "\n")


# takes in array of sections and turns them into section classes
def buildSchedule(coursesArray):
    # next(iter(course.values())) helps with getting the value of the first key
    parsedCoursesArray = []
    coursesArray = sorted(coursesArray, key=len)
    for course in coursesArray:
        parsedCoursesArray.append(
                sectionClass.Section(next(iter(course.values()))))
    schedulize(parsedCoursesArray)

