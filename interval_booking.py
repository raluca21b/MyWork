def converteStringToMinutes(interval):
    """
    The function converte the value of string hour given into integer value of the minutes representig
    :param interval: list of 2 string elements representig the start and end hour of a booked interval
    :return: intevalConverted: list of 2 integers representig the integer value of the hour
    """
    intervalConverted = []
    minutesStart = interval[0].split(':')
    intervalConverted.append(int(minutesStart[0])*60 + int(minutesStart[1]))
    minutesEnd = interval[1].split(':')
    intervalConverted.append(int(minutesEnd[0]) * 60 + int(minutesEnd[1]))
    return intervalConverted

def findAvailableIntervals(booked1,limits1,booked2,limits2,meetingTime):
    """
    Function finds the available intervals of time for 2 people to meet
    :param booked1: the intervals booked for the first person
    :param limits1: the intervals of the calendar for the first person
    :param booked2: the intervals booked for the second person
    :param limits2: the intervals of the calendar for the second person
    :param meetingTime: the length of the meeting
    :return: availableIntervals: list of the free intervals of the day for both people
    """
    #  the limits as a booking interval
    startAvailable = max(limits1[0],limits2[0])
    lastAvailable = min(limits1[1],limits2[1])


    booked = booked1 + booked2 #reunite the all the booked interval into one single list
    booked.sort()#sorting the list so the intervals will be in ascending order

    availableIntervals =[]
    for interval in booked:#take each interval
        if interval[0] > startAvailable:#if the current interval starts after the available start:
            end = interval[0]           #mark the end of the disponible time
            if end - startAvailable >= meetingTime:   #if the gap is favorable to set a meeting
                availableIntervals.append([startAvailable,end]) #mark the interval as available
            startAvailable = interval[1]      #set the next available start time (the current's interval end time)
        elif interval[1] <= startAvailable:   #if the current interval ends before the available start, the search continues with another interval
            continue
        else:                                #any other way, update the next available start time
            startAvailable = interval[1]

    ##if the last interval ends before the last available time:
    if lastAvailable > startAvailable and lastAvailable - startAvailable >= meetingTime:
        availableIntervals.append([startAvailable,lastAvailable])          #add the interval as available

    #converte the list back into string format
    availableIntervalsString = [[f"{interval[0]//60:02d}:{interval[0]%60:02d}",f"{interval[1]//60:02d}:{interval[1]%60:02d}"]
                          for interval in availableIntervals]
    return availableIntervalsString



def main():
    bookedCalendar1 = [['9:00','10:30'],['12:00','13:00'],['16:00','18:00']]
    calendarLimits1 = ['9:00','20:00']
    bookedCalendar2 = [['10:00','11:30'],['12:30','14:30'],['14:30','15:00'],['16:00','17:00']]
    calendarLimits2 = ['10:00','18:30']
    meetingTimeMinutes = 30

    #converte the intervals given
    booked1 = [converteStringToMinutes(interval) for interval in bookedCalendar1]
    limits1 = converteStringToMinutes(calendarLimits1)
    booked2 = [converteStringToMinutes(interval) for interval in bookedCalendar2]
    limits2 = converteStringToMinutes(calendarLimits2)
    availableIntervals = findAvailableIntervals(booked1,limits1,booked2,limits2,meetingTimeMinutes)
    print("The available intervals for meetings are: ",availableIntervals)
main()