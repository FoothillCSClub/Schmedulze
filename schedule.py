import classie
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
    obj = classie.Classie(classExample)
    print(obj.times)

if __name__ == '__main__':
    main()
