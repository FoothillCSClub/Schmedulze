import classie
import schedClass

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
    classExample2 = [
        {
          "CRN": "40153", 
          "campus": "FH", 
          "course": "MATH F010.01Y", 
          "days": "M", 
          "desc": "ELEMENTARY STATISTICS", 
          "end": "06/29/2018", 
          "instructor": "Martinez", 
          "room": "5502", 
          "seats": "80", 
          "start": "04/09/2018", 
          "status": "Open", 
          "time": "08:00 AM-09:30 AM", 
          "units": "  5.00", 
          "wait_cap": "10", 
          "wait_seats": "10"
            } 
        ]
    obj = classie.Section(classExample)
    obj2 = classie.Section(classExample2)
    print(schedClass.isOverLapping([obj], obj2))

if __name__ == '__main__':
    main()
