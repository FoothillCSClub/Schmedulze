import scheduleLogic


def main():
    class1 = {
  "40151": [
    {
      "CRN": "40151", 
      "campus": "FH", 
      "course": "MATH F002A01", 
      "days": "MW", 
      "desc": "DIFFERENTIAL EQUATIONS", 
      "end": "06/29/2018", 
      "instructor": "Park Lee", 
      "room": "4601", 
      "seats": "40", 
      "start": "04/09/2018", 
      "status": "Open", 
      "time": "08:00 AM-09:50 AM", 
      "units": "  5.00", 
      "wait_cap": "10", 
      "wait_seats": "10"
    }, 
    {
      "CRN": "40151", 
      "campus": "FH", 
      "course": "MATH F002A01", 
      "days": "F", 
      "desc": "DIFFERENTIAL EQUATIONS", 
      "end": "06/29/2018", 
      "instructor": "Park Lee", 
      "room": "4601", 
      "seats": "40", 
      "start": "04/09/2018", 
      "status": "Open", 
      "time": "08:00 AM-08:50 AM", 
      "units": "  5.00", 
      "wait_cap": "10", 
      "wait_seats": "10"
    }
  ], 
  "40433": [
    {
      "CRN": "40433", 
      "campus": "FH", 
      "course": "MATH F002A02", 
      "days": "TTh", 
      "desc": "DIFFERENTIAL EQUATIONS", 
      "end": "06/29/2018", 
      "instructor": "Park Lee", 
      "room": "5610", 
      "seats": "40", 
      "start": "04/09/2018", 
      "status": "Open", 
      "time": "10:00 AM-11:50 AM", 
      "units": "  5.00", 
      "wait_cap": "10", 
      "wait_seats": "10"
    }, 
    {
      "CRN": "40433", 
      "campus": "FH", 
      "course": "MATH F002A02", 
      "days": "F", 
      "desc": "DIFFERENTIAL EQUATIONS", 
      "end": "06/29/2018", 
      "instructor": "Park Lee", 
      "room": "5610", 
      "seats": "40", 
      "start": "04/09/2018", 
      "status": "Open", 
      "time": "11:00 AM-11:50 AM", 
      "units": "  5.00", 
      "wait_cap": "10", 
      "wait_seats": "10"
    }
  ], 
  "40518": [
    {
      "CRN": "40518", 
      "campus": "FH", 
      "course": "MATH F002A03", 
      "days": "MW", 
      "desc": "DIFFERENTIAL EQUATIONS", 
      "end": "06/29/2018", 
      "instructor": "Park Lee", 
      "room": "4603", 
      "seats": "40", 
      "start": "04/09/2018", 
      "status": "Open", 
      "time": "06:00 PM-08:15 PM", 
      "units": "  5.00", 
      "wait_cap": "10", 
      "wait_seats": "10"
    }
  ]
} 

    class2 =   {
    "40158": [
    {
      "CRN": "40158",
      "campus": "FH",
      "course": "MATH F022.01",
      "days": "MW",
      "desc": "DISCRETE MATHEMATICS",
      "end": "06/29/2018",
      "instructor": "Morriss",
      "room": "4502",
      "seats": "35",
      "start": "04/09/2018",
      "status": "Open",
      "time": "01:30 PM-03:45 PM",
      "units": "  5.00",
      "wait_cap": "10",
      "wait_seats": "10"
    }
  ],
  "40455": [
    {
      "CRN": "40455",
      "campus": "FH",
      "course": "MATH F022.02",
      "days": "MW",
      "desc": "DISCRETE MATHEMATICS",
      "end": "06/29/2018",
      "instructor": "Witschorik",
      "room": "5609",
      "seats": "40",
      "start": "04/09/2018",
      "status": "Open",
      "time": "06:00 PM-08:15 PM",
      "units": "  5.00",
      "wait_cap": "0",
      "wait_seats": "0"
    }
  ]
}

    class3 = {
  "40408": [
    {
      "CRN": "40408", 
      "campus": "FH", 
      "course": "C S F010.01Y", 
      "days": "TTh", 
      "desc": "COMPUTER ARCHITEC/ORGANIZATION", 
      "end": "06/29/2018", 
      "instructor": "Riordan", 
      "room": "4308", 
      "seats": "40", 
      "start": "04/09/2018", 
      "status": "Open", 
      "time": "06:30 PM-08:20 PM", 
      "units": "  4.50", 
      "wait_cap": "10", 
      "wait_seats": "10"
    }, 
    {
      "CRN": "40408", 
      "campus": "FH", 
      "course": "C S F010.01Y", 
      "days": "TBA", 
      "desc": "COMPUTER ARCHITEC/ORGANIZATION", 
      "end": "06/29/2018", 
      "instructor": "Riordan", 
      "room": "ONLINE", 
      "seats": "40", 
      "start": "04/09/2018", 
      "status": "Open", 
      "time": "TBA", 
      "units": "  4.50", 
      "wait_cap": "10", 
      "wait_seats": "10"
    }
  ], 
    "40890": [
    {
      "CRN": "40890", 
      "campus": "FH", 
      "course": "C S F010.02W", 
      "days": "TBA", 
      "desc": "COMPUTER ARCHITEC/ORGANIZATION", 
      "end": "06/29/2018", 
      "instructor": "Lamble", 
      "room": "ONLINE", 
      "seats": "40", 
      "start": "04/09/2018", 
      "status": "Open", 
      "time": "TBA", 
      "units": "  4.50", 
      "wait_cap": "10", 
      "wait_seats": "10"
    }
    ]}
    classes = [class1, class2, class3]
    scheduleLogic.buildSchedule(classes)   


if __name__ == '__main__':
    main()
