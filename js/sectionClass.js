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
	var [startTime, endTime] = time_str.split('-')
	startTime = parse_minutes(startTime)
	endTime = parse_minutes(endTime)
	var indexOfThursday = days_str.substring("Th")
	if(indexOfThursday != -1)
	{
		var thursdayInMin = dayInMinutes * 3
		time.concat([startTime + thursdayInMin ,     endTime + thursdayInMin])
	}
	for(day in day_str)
	{
		var addDayMin = 0
		switch(day)
		{
			case "M":
				addDayMin = 0
				break;
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
		time.concat([startTime + addDayMin, endTime + addDayMin])
	}
}

class Section 
{
	constructor(classObj)
	{
		this.crn = classObj[0]['CRN']
		this.times = []
		for(singleClass in classObj)
		{
			var timeOfClass = parse_time(classObj[singleClass]['time'], classObj[singleClass]['days'])
			if(timeOfClass)
			{
				for(time in timeOfClass)
				{
					this.times.concat(timeOfClass[time])
				}
			}
		}
	}
}
