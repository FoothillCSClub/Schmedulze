import scheduleLogic


def main():
    class1 = {
          "40140": [
            {
              "CRN": "40140", 
              "campus": "FH", 
              "course": "ENGL F001A01", 
              "days": "MW", 
              "desc": "COMPOSITION & READING", 
              "end": "06/29/2018", 
              "instructor": "Bachman", 
              "room": "6305", 
              "seats": "30", 
              "start": "04/09/2018", 
              "status": "Open", 
              "time": "07:35 AM-09:50 AM", 
              "units": "  5.00", 
              "wait_cap": "15", 
              "wait_seats": "15"
            }
          ], 
          "40141": [
            {
              "CRN": "40141", 
              "campus": "FH", 
              "course": "ENGL F001A03", 
              "days": "MW", 
              "desc": "COMPOSITION & READING", 
              "end": "06/29/2018", 
              "instructor": "Mills", 
              "room": "6409", 
              "seats": "30", 
              "start": "04/09/2018", 
              "status": "Open", 
              "time": "08:00 AM-09:50 AM", 
              "units": "  5.00", 
              "wait_cap": "15", 
              "wait_seats": "15"
            }, 
            {
              "CRN": "40141", 
              "campus": "FH", 
              "course": "ENGL F001A03", 
              "days": "F", 
              "desc": "COMPOSITION & READING", 
              "end": "06/29/2018", 
              "instructor": "Mills", 
              "room": "6409", 
              "seats": "30", 
              "start": "04/09/2018", 
              "status": "Open", 
              "time": "08:00 AM-08:50 AM", 
              "units": "  5.00", 
              "wait_cap": "15", 
              "wait_seats": "15"
            }
          ]}

    class2 = { 
            "40270": [
            {
              "CRN": "40270", 
              "campus": "FH", 
              "course": "ENGL F001B02", 
              "days": "TTh", 
              "desc": "COMP/CRIT READ/THINK LITERATUR", 
              "end": "06/29/2018", 
              "instructor": "Goldstone", 
              "room": "6405", 
              "seats": "30", 
              "start": "04/09/2018", 
              "status": "Open", 
              "time": "07:35 AM-09:50 AM", 
              "units": "  5.00", 
              "wait_cap": "15", 
              "wait_seats": "15"
            }
            ]}

    classes = [class1, class2]
    scheduleLogic.buildSchedule(classes)   


if __name__ == '__main__':
    main()
