#Michelle Yick
#12-12-2014
#Functions class exercises. Development Q1.

#Convert minutes to seconds:
def convert_minutes_to_seconds(minutes,seconds):
    total = minutes*60
    return total

#Convert hours to minutes:
def convert_hours_to_seconds(hours,seconds):
    total = hours*60*60
    return total

#Calculate the full amount of seconds:
def full_calculation(seconds,minutes,hours):
    total = seconds + convert_hours_to_seconds(hours,seconds) + convert_minutes_to_seconds(minutes,seconds)
    return total

#Input seconds, minutes and hours:
def input_seconds_minutes_hours():
    hours = int(input("Enter the number of hours"))
    minutes = int(input("Enter the number of minutes"))
    seconds = int(input("Enter the number of seconds"))
    return hours,minutes,seconds

#Printing the total:
def display_total_in_seconds(total):
    print(total)

#Main program:
def convert_hours_minutes_seconds_to_seconds():
    hours,minutes,seconds = input_seconds_minutes_hours()
    total = full_calculation(seconds,minutes,hours)
    display_total_in_seconds(total)
convert_hours_minutes_seconds_to_seconds()



    
