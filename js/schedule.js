//SECTION CLASS -------------------------------------------------------
function parse_minutes(time_str)
{
	var hour = time_str.substring(0,2)
	var min = time_str.substring(3,5)
	var time = parseInt(hour) * 60 + parseInt(min)
	if(time_str.substring(6,8) == "PM")
	{
		return time + 720
	}
	else
	{
		return time
	}
}

function parse_time(time_str, days_str)
{
	if(days_str.indexOf("TBA") != -1)
	{
		return
	}
	var dayInMinutes = 1440
	var time = []
	var [startTime, endTime] = time_str.split('-')
	startTime = parse_minutes(startTime)
	endTime = parse_minutes(endTime)
	if(days_str.indexOf("Th") != -1)
	{
		var thursdayInMin = dayInMinutes * 3
		days_str = days_str.replace("Th",'')
		time.push([startTime + thursdayInMin, endTime + thursdayInMin])
	}
	for(day in days_str)
	{
		var addDayMin = 0
		switch(days_str[day])
		{
			case "T":
				addDayMin = dayInMinutes
				break;
			case "W":
				addDayMin = dayInMinutes * 2
				break;
			case "R":
				addDayMin = dayInMinutes * 3
				break;
			case "F":
				addDayMin = dayInMinutes * 4
				break;
			case "S":
				addDayMin = dayInMinutes * 5
				break;
			case "U":
				addDayMin = dayInMinutes * 6
				break;	
		}
		time.push([startTime + addDayMin, endTime + addDayMin])
	}
	return time
}

class Section 
{
	constructor(classObj)
	{
		this.crn = classObj[0]["CRN"]
		var timeTemp = []
		classObj.forEach(function (section)
		{
			var timeOfClass = parse_time(section["time"], section["days"])
			if(timeOfClass)
			{
				timeTemp.push(timeOfClass)
			}
		})
		this.time = timeTemp
	}
}

//SECTION CLASS -------------------------------------------------------




//LOGIC ---------------------------------------------------------------
function isOverLapping(cur_schedule, addClass)
{
	newSchedule = []
	for(section in cur_schedule)
	{
		newSchedule.push(cur_schedule[section].times)
	}
	newSchedule.push(addClass.times)
}

function buildSchedule(coursesInput)
{
	coursesInput.sort(function(course1, course2)
	{
		return Object.keys(course1).length - Object.keys(course2).length
	})
	var parsedCoursesArray = []
	for(course in coursesInput)
	{
		courseArray = []
		for(section in coursesInput[course])
		{
			courseArray.push(new Section(coursesInput[course][section]))
		}
		parsedCoursesArray.push(courseArray)
	}
	console.log(parsedCoursesArray)
	//schedulize(parsedCoursesArray)
}
//LOGIC ---------------------------------------------------------------




//INPUT TO LOGIC -----------------------------------------------------


let input2 = {
      "40153": [
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
        }, 
        {
          "CRN": "40153", 
          "campus": "FH", 
          "course": "MATH F010.01Y", 
          "days": "TBA", 
          "desc": "ELEMENTARY STATISTICS", 
          "end": "06/29/2018", 
          "instructor": "Martinez", 
          "room": "ONLINE", 
          "seats": "80", 
          "start": "04/09/2018", 
          "status": "Open", 
          "time": "TBA", 
          "units": "  5.00", 
          "wait_cap": "10", 
          "wait_seats": "10"
        }
      ], 
      "40156": [
        {
          "CRN": "40156", 
          "campus": "FH", 
          "course": "MATH F010.03W", 
          "days": "TBA", 
          "desc": "ELEMENTARY STATISTICS", 
          "end": "06/29/2018", 
          "instructor": "Low", 
          "room": "ONLINE", 
          "seats": "40", 
          "start": "04/09/2018", 
          "status": "Open", 
          "time": "TBA", 
          "units": "  5.00", 
          "wait_cap": "10", 
          "wait_seats": "10"
        }
      ], 
      "40312": [
        {
          "CRN": "40312", 
          "campus": "FH", 
          "course": "MATH F010.08W", 
          "days": "TBA", 
          "desc": "ELEMENTARY STATISTICS", 
          "end": "06/29/2018", 
          "instructor": "Martinez", 
          "room": "ONLINE", 
          "seats": "80", 
          "start": "04/09/2018", 
          "status": "Open", 
          "time": "TBA", 
          "units": "  5.00", 
          "wait_cap": "10", 
          "wait_seats": "10"
        }
      ], 
      "40335": [
        {
          "CRN": "40335", 
          "campus": "FH", 
          "course": "MATH F010.02", 
          "days": "TTh", 
          "desc": "ELEMENTARY STATISTICS", 
          "end": "06/29/2018", 
          "instructor": "Munoz", 
          "room": "5601", 
          "seats": "40", 
          "start": "04/09/2018", 
          "status": "Open", 
          "time": "08:00 AM-09:50 AM", 
          "units": "  5.00", 
          "wait_cap": "10", 
          "wait_seats": "10"
        }, 
        {
          "CRN": "40335", 
          "campus": "FH", 
          "course": "MATH F010.02", 
          "days": "F", 
          "desc": "ELEMENTARY STATISTICS", 
          "end": "06/29/2018", 
          "instructor": "Munoz", 
          "room": "5601", 
          "seats": "40", 
          "start": "04/09/2018", 
          "status": "Open", 
          "time": "09:00 AM-09:50 AM", 
          "units": "  5.00", 
          "wait_cap": "10", 
          "wait_seats": "10"
        }
      ], 
      "40374": [
        {
          "CRN": "40374", 
          "campus": "FH", 
          "course": "MATH F010.07", 
          "days": "TTh", 
          "desc": "ELEMENTARY STATISTICS", 
          "end": "06/29/2018", 
          "instructor": "Morriss", 
          "room": "4604", 
          "seats": "40", 
          "start": "04/09/2018", 
          "status": "Open", 
          "time": "01:30 PM-03:45 PM", 
          "units": "  5.00", 
          "wait_cap": "10", 
          "wait_seats": "10"
        }
      ], 
      "40375": [
        {
          "CRN": "40375", 
          "campus": "FH", 
          "course": "MATH F010.09W", 
          "days": "TBA", 
          "desc": "ELEMENTARY STATISTICS", 
          "end": "06/29/2018", 
          "instructor": "Seelbach", 
          "room": "ONLINE", 
          "seats": "40", 
          "start": "04/09/2018", 
          "status": "Open", 
          "time": "TBA", 
          "units": "  5.00", 
          "wait_cap": "10", 
          "wait_seats": "10"
        }
      ], 
      "40519": [
        {
          "CRN": "40519", 
          "campus": "FH", 
          "course": "MATH F010.06", 
          "days": "TThF", 
          "desc": "ELEMENTARY STATISTICS", 
          "end": "06/29/2018", 
          "instructor": "Francisco", 
          "room": "4310", 
          "seats": "40", 
          "start": "04/09/2018", 
          "status": "Open", 
          "time": "12:00 PM-01:25 PM", 
          "units": "  5.00", 
          "wait_cap": "10", 
          "wait_seats": "10"
        }
      ], 
      "40523": [
        {
          "CRN": "40523", 
          "campus": "FH", 
          "course": "MATH F010.04", 
          "days": "F", 
          "desc": "ELEMENTARY STATISTICS", 
          "end": "06/29/2018", 
          "instructor": "Tomutiu", 
          "room": "4606", 
          "seats": "40", 
          "start": "04/09/2018", 
          "status": "Open", 
          "time": "10:00 AM-10:50 AM", 
          "units": "  5.00", 
          "wait_cap": "10", 
          "wait_seats": "10"
        }, 
        {
          "CRN": "40523", 
          "campus": "FH", 
          "course": "MATH F010.04", 
          "days": "MW", 
          "desc": "ELEMENTARY STATISTICS", 
          "end": "06/29/2018", 
          "instructor": "Tomutiu", 
          "room": "4606", 
          "seats": "40", 
          "start": "04/09/2018", 
          "status": "Open", 
          "time": "10:00 AM-11:50 AM", 
          "units": "  5.00", 
          "wait_cap": "10", 
          "wait_seats": "10"
        }
      ], 
      "40525": [
        {
          "CRN": "40525", 
          "campus": "FC", 
          "course": "MATH F010.50", 
          "days": "MW", 
          "desc": "ELEMENTARY STATISTICS", 
          "end": "06/29/2018", 
          "instructor": "Butterworth", 
          "room": "SV204", 
          "seats": "40", 
          "start": "04/09/2018", 
          "status": "Open", 
          "time": "06:00 PM-08:15 PM", 
          "units": "  5.00", 
          "wait_cap": "10", 
          "wait_seats": "10"
        }
      ], 
      "40731": [
        {
          "CRN": "40731", 
          "campus": "FH", 
          "course": "MATH F010.10W", 
          "days": "TBA", 
          "desc": "ELEMENTARY STATISTICS", 
          "end": "06/29/2018", 
          "instructor": "Maskalevich", 
          "room": "ONLINE", 
          "seats": "40", 
          "start": "04/09/2018", 
          "status": "Open", 
          "time": "TBA", 
          "units": "  5.00", 
          "wait_cap": "10", 
          "wait_seats": "10"
        }
      ], 
      "40755": [
        {
          "CRN": "40755", 
          "campus": "FH", 
          "course": "MATH F010.05", 
          "days": "F", 
          "desc": "ELEMENTARY STATISTICS", 
          "end": "06/29/2018", 
          "instructor": "Morriss", 
          "room": "4606", 
          "seats": "40", 
          "start": "04/09/2018", 
          "status": "Open", 
          "time": "11:00 AM-11:50 AM", 
          "units": "  5.00", 
          "wait_cap": "10", 
          "wait_seats": "10"
        }, 
        {
          "CRN": "40755", 
          "campus": "FH", 
          "course": "MATH F010.05", 
          "days": "TTh", 
          "desc": "ELEMENTARY STATISTICS", 
          "end": "06/29/2018", 
          "instructor": "Morriss", 
          "room": "4606", 
          "seats": "40", 
          "start": "04/09/2018", 
          "status": "Open", 
          "time": "10:00 AM-11:50 AM", 
          "units": "  5.00", 
          "wait_cap": "10", 
          "wait_seats": "10"
        }
      ], 
      "40903": [
        {
          "CRN": "40903", 
          "campus": "FH", 
          "course": "MATH F010.11W", 
          "days": "TBA", 
          "desc": "ELEMENTARY STATISTICS", 
          "end": "06/29/2018", 
          "instructor": "Maskalevich", 
          "room": "ONLINE", 
          "seats": "40", 
          "start": "04/09/2018", 
          "status": "Open", 
          "time": "TBA", 
          "units": "  5.00", 
          "wait_cap": "10", 
          "wait_seats": "10"
        }
      ], 
      "41912": [
        {
          "CRN": "41912", 
          "campus": "FH", 
          "course": "MATH F010.12", 
          "days": "MW", 
          "desc": "ELEMENTARY STATISTICS", 
          "end": "06/29/2018", 
          "instructor": "Papay", 
          "room": "4601", 
          "seats": "40", 
          "start": "04/09/2018", 
          "status": "Open", 
          "time": "01:30 PM-03:45 PM", 
          "units": "  5.00", 
          "wait_cap": "10", 
          "wait_seats": "10"
        }
      ], 
      "42060": [
        {
          "CRN": "42060", 
          "campus": "FH", 
          "course": "MATH F010.13W", 
          "days": "TBA", 
          "desc": "ELEMENTARY STATISTICS", 
          "end": "06/29/2018", 
          "instructor": "Staff", 
          "room": "ONLINE", 
          "seats": "40", 
          "start": "05/21/2018", 
          "status": "Open", 
          "time": "TBA", 
          "units": "  5.00", 
          "wait_cap": "10", 
          "wait_seats": "10"
        }
      ], 
      "42157": [
        {
          "CRN": "42157", 
          "campus": "FH", 
          "course": "MATH F010.14W", 
          "days": "TBA", 
          "desc": "ELEMENTARY STATISTICS", 
          "end": "06/29/2018", 
          "instructor": "Low", 
          "room": "ONLINE", 
          "seats": "40", 
          "start": "04/09/2018", 
          "status": "Open", 
          "time": "TBA", 
          "units": "  5.00", 
          "wait_cap": "10", 
          "wait_seats": "10"
        }
      ], 
      "42224": [
        {
          "CRN": "42224", 
          "campus": "FH", 
          "course": "MATH F010.15W", 
          "days": "TBA", 
          "desc": "ELEMENTARY STATISTICS", 
          "end": "06/29/2018", 
          "instructor": "Seelbach", 
          "room": "ONLINE", 
          "seats": "40", 
          "start": "04/09/2018", 
          "status": "Open", 
          "time": "TBA", 
          "units": "  5.00", 
          "wait_cap": "10", 
          "wait_seats": "10"
        }
      ], 
      "42227": [
        {
          "CRN": "42227", 
          "campus": "FC", 
          "course": "MATH F010.07Y", 
          "days": "F", 
          "desc": "ELEMENTARY STATISTICS", 
          "end": "06/29/2018", 
          "instructor": "Staff", 
          "room": "", 
          "seats": "0", 
          "start": "04/09/2018", 
          "status": "Full", 
          "time": "11:00 AM-12:15 PM", 
          "units": "  5.00", 
          "wait_cap": "0", 
          "wait_seats": "0"
        }, 
        {
          "CRN": "42227", 
          "campus": "", 
          "course": "MATH F010.07Y", 
          "days": "TBA", 
          "desc": "ELEMENTARY STATISTICS", 
          "end": "06/29/2018", 
          "instructor": "Staff", 
          "room": "", 
          "seats": "0", 
          "start": "04/09/2018", 
          "status": "Full", 
          "time": "TBA", 
          "units": "  5.00", 
          "wait_cap": "0", 
          "wait_seats": "0"
        }
      ]
    }

let input3 = {
      "40264": [
        {
          "CRN": "40264", 
          "campus": "FH", 
          "course": "ENGL F110.05", 
          "days": "TTh", 
          "desc": "INTRO TO COLLEGE WRITING", 
          "end": "06/29/2018", 
          "instructor": "Fernandez", 
          "room": "6409", 
          "seats": "25", 
          "start": "04/09/2018", 
          "status": "Open", 
          "time": "10:00 AM-11:50 AM", 
          "units": "  5.00", 
          "wait_cap": "15", 
          "wait_seats": "15"
        }, 
        {
          "CRN": "40264", 
          "campus": "FH", 
          "course": "ENGL F110.05", 
          "days": "F", 
          "desc": "INTRO TO COLLEGE WRITING", 
          "end": "06/29/2018", 
          "instructor": "Fernandez", 
          "room": "6409", 
          "seats": "25", 
          "start": "04/09/2018", 
          "status": "Open", 
          "time": "11:00 AM-11:50 AM", 
          "units": "  5.00", 
          "wait_cap": "15", 
          "wait_seats": "15"
        }
      ], 
      "40265": [
        {
          "CRN": "40265", 
          "campus": "FH", 
          "course": "ENGL F110.06", 
          "days": "TThF", 
          "desc": "INTRO TO COLLEGE WRITING", 
          "end": "06/29/2018", 
          "instructor": "Dauer", 
          "room": "6305", 
          "seats": "25", 
          "start": "04/09/2018", 
          "status": "Open", 
          "time": "12:00 PM-01:25 PM", 
          "units": "  5.00", 
          "wait_cap": "15", 
          "wait_seats": "15"
        }
      ], 
      "40437": [
        {
          "CRN": "40437", 
          "campus": "FH", 
          "course": "ENGL F110.04", 
          "days": "MW", 
          "desc": "INTRO TO COLLEGE WRITING", 
          "end": "06/29/2018", 
          "instructor": "Armerding", 
          "room": "6503", 
          "seats": "25", 
          "start": "04/09/2018", 
          "status": "Open", 
          "time": "10:00 AM-11:50 AM", 
          "units": "  5.00", 
          "wait_cap": "15", 
          "wait_seats": "15"
        }, 
        {
          "CRN": "40437", 
          "campus": "FH", 
          "course": "ENGL F110.04", 
          "days": "F", 
          "desc": "INTRO TO COLLEGE WRITING", 
          "end": "06/29/2018", 
          "instructor": "Armerding", 
          "room": "", 
          "seats": "25", 
          "start": "04/09/2018", 
          "status": "Open", 
          "time": "10:00 AM-10:50 AM", 
          "units": "  5.00", 
          "wait_cap": "15", 
          "wait_seats": "15"
        }
      ], 
      "40481": [
        {
          "CRN": "40481", 
          "campus": "FH", 
          "course": "ENGL F110.01", 
          "days": "MW", 
          "desc": "INTRO TO COLLEGE WRITING", 
          "end": "06/29/2018", 
          "instructor": "Escamilla", 
          "room": "6405", 
          "seats": "25", 
          "start": "04/09/2018", 
          "status": "Open", 
          "time": "07:35 AM-09:50 AM", 
          "units": "  5.00", 
          "wait_cap": "15", 
          "wait_seats": "15"
        }
      ], 
      "40482": [
        {
          "CRN": "40482", 
          "campus": "FH", 
          "course": "ENGL F110.03", 
          "days": "F", 
          "desc": "INTRO TO COLLEGE WRITING", 
          "end": "06/29/2018", 
          "instructor": "Hoffer", 
          "room": "6307", 
          "seats": "25", 
          "start": "04/09/2018", 
          "status": "Open", 
          "time": "09:00 AM-09:50 AM", 
          "units": "  5.00", 
          "wait_cap": "15", 
          "wait_seats": "15"
        }, 
        {
          "CRN": "40482", 
          "campus": "FH", 
          "course": "ENGL F110.03", 
          "days": "TTh", 
          "desc": "INTRO TO COLLEGE WRITING", 
          "end": "06/29/2018", 
          "instructor": "Hoffer", 
          "room": "6307", 
          "seats": "25", 
          "start": "04/09/2018", 
          "status": "Open", 
          "time": "08:00 AM-09:50 AM", 
          "units": "  5.00", 
          "wait_cap": "15", 
          "wait_seats": "15"
        }
      ], 
      "40650": [
        {
          "CRN": "40650", 
          "campus": "FH", 
          "course": "ENGL F110.02", 
          "days": "F", 
          "desc": "INTRO TO COLLEGE WRITING", 
          "end": "06/29/2018", 
          "instructor": "Folk", 
          "room": "6301", 
          "seats": "25", 
          "start": "04/09/2018", 
          "status": "Open", 
          "time": "08:00 AM-08:50 AM", 
          "units": "  5.00", 
          "wait_cap": "15", 
          "wait_seats": "15"
        }, 
        {
          "CRN": "40650", 
          "campus": "FH", 
          "course": "ENGL F110.02", 
          "days": "MW", 
          "desc": "INTRO TO COLLEGE WRITING", 
          "end": "06/29/2018", 
          "instructor": "Folk", 
          "room": "6301", 
          "seats": "25", 
          "start": "04/09/2018", 
          "status": "Open", 
          "time": "08:00 AM-09:50 AM", 
          "units": "  5.00", 
          "wait_cap": "15", 
          "wait_seats": "15"
        }
      ], 
      "41070": [
        {
          "CRN": "41070", 
          "campus": "FH", 
          "course": "ENGL F110.07", 
          "days": "TTh", 
          "desc": "INTRO TO COLLEGE WRITING", 
          "end": "06/29/2018", 
          "instructor": "Mcdonald", 
          "room": "6301", 
          "seats": "25", 
          "start": "04/09/2018", 
          "status": "Open", 
          "time": "01:30 PM-03:45 PM", 
          "units": "  5.00", 
          "wait_cap": "5", 
          "wait_seats": "5"
        }
      ]
    }

let	input1 = {
      "41320": [
        {
          "CRN": "41320", 
          "campus": "FH", 
          "course": "PHYS F012.01", 
          "days": "MW", 
          "desc": "INTRO TO MODERN PHYSICS", 
          "end": "06/29/2018", 
          "instructor": "Marasco", 
          "room": "5015", 
          "seats": "85", 
          "start": "04/09/2018", 
          "status": "Open", 
          "time": "10:00 AM-11:50 AM", 
          "units": "  5.00", 
          "wait_cap": "10", 
          "wait_seats": "10"
        }, 
        {
          "CRN": "41320", 
          "campus": "FH", 
          "course": "PHYS F012.01", 
          "days": "F", 
          "desc": "INTRO TO MODERN PHYSICS", 
          "end": "06/29/2018", 
          "instructor": "Marasco", 
          "room": "5015", 
          "seats": "85", 
          "start": "04/09/2018", 
          "status": "Open", 
          "time": "10:00 AM-10:50 AM", 
          "units": "  5.00", 
          "wait_cap": "10", 
          "wait_seats": "10"
        }
      ]
    }

inputs = [input2, input3, input1]
buildSchedule(inputs)

//INPUT TO LOGIC -----------------------------------------------------
