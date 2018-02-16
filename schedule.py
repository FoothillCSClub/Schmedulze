def get_sec(time_str):
    h, m = time_str[:-3].split(':')
    if(time_str[-2:] == "PM"):
        return int(h) * 60 + int(m) + 720
    else:
        return int(h) * 60 + int(m)

def doesItFit(class1, class2):

def sort(schedule, otherClasses):




def main():
    classes = [{"time": "10:00 AM-01:50 PM", "CRN": "40157"}, {"time": "08:00 AM-11:50 AM","CRN":"40388"}]
    for classie in classes:
        startTime, endTime = classie["time"].split('-')
        startTime = get_sec(startTime)
        endTime = get_sec(endTime)
        classie['startMin'] = startTime
        classie['endMin'] = endTime
    print(classes)

if __name__ == '__main__':
    main()
