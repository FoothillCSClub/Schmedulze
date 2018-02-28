import sectionClass
import copy

def isOverLapping(classArr, classArr2):
    newSchedule = []
    for section in classArr:
        newSchedule += section.times
    newSchedule += classArr2.times
    newSchedule = sorted(newSchedule, key=lambda x: x[0])
    for i in range(1, len(newSchedule) - 1):
        if(newSchedule[i-1][1] > newSchedule[i][0]):
            return True
        return False


def findPossibleSchedule(schedule, otherCourses, possibleSchedules):
    if len(otherCourses) <= 0:
        print(schedule)
        if schedule == False :
            return False
        possibleSchedules.append(schedule)
        return True
    for section in otherCourses[0]:
        condition = isOverLapping(schedule, section)
        if not condition:
            print(type(schedule), type(section))
            schedule = schedule.extend(section)
            print(schedule)
            findPossibleSchedule(schedule,
            otherCourses[1:], possibleSchedules)
        else:
            findPossibleSchedule(False, [], [])
    return


def schedulize(parsedCoursesArray):
    possibleSchedules = []
    for course in parsedCoursesArray:
        print("\n------New Course------\n")
        for section in course:
            print("Section CRN:", section)
    print("\n\n")
    for section in parsedCoursesArray[0]:
        sectionArr = []
        sectionArr.append(section)
        findPossibleSchedule(sectionArr, parsedCoursesArray[1:],
                copy.deepcopy(possibleSchedules))
    for schedule in possibleSchedules:
        print("possible schdule ", schedule)


# takes in array of sections and turns them into section classes
def buildSchedule(coursesArray):
    # next(iter(course.values())) helps with getting the value of the first key
    parsedCoursesArray = []
    coursesArray = sorted(coursesArray, key=lambda k: len(k.keys()))
    print("Sorted List:\n")
    for course in coursesArray:
        print(course, "\n")
        sectionsArray = []
        for key, value in course.items():
            sectionsArray.append(sectionClass.Section(value))
        parsedCoursesArray.append(sectionsArray)
    schedulize(parsedCoursesArray)
