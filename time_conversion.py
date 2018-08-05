#Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

#Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock.
#Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.
#Test case1: Input: 07:05:45PM Output: 19:05:45
#Test case2: Input: 06:40:03AM Output: 06:40:03
#Test case3: Input: 12:45:54PM Output: 12:45:54

def timeConversion(time):
    if time[-2:] == "AM" and time[:2] == "12":
        return "00" + time[2:8]
    elif time[-2:] == "AM":
        return time[:8]
    elif time[-2:] == "PM" and time[:2] == "12":
        return time[:8]
    else:
        return str(int(time[:2])+12) + time[2:8]

time = input()
print(timeConversion(time))
