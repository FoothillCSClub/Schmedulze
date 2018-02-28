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

"""
@schedule: list of sections which we try to fill with one section from
           each course in @otherCourses. Initially contains one section,
           passed in from schedulize()
@otherCourses: list of courses which we try to schedule
@possibleSchedules: call by reference output parameter; hopefully we
                    populate it with a list of possible schedules.
"""
def findPossibleSchedule(schedule: list, otherCourses: list, possibleSchedules: list):

    if len(otherCourses) == 0:
        possibleSchedules.append(schedule)
        return

    for section in otherCourses[0]:

        cur_schedule = list(schedule)

        if not isOverLapping(cur_schedule, section):
            cur_schedule.append(section)

            findPossibleSchedule(
                cur_schedule,
                otherCourses[1:],
                possibleSchedules
            )

def schedulize(parsedCoursesArray):
    possibleSchedules = []

    for course in parsedCoursesArray:
        print("\n------New Course------\n")
        for section in course:
            print("Section CRN:", section)
    print("\n\n")

    for section in parsedCoursesArray[0]:
        sectionArr = [section]
        findPossibleSchedule(
            sectionArr,
            parsedCoursesArray[1:],
            possibleSchedules
        )

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
