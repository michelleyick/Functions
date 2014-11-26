#Michelle Yick
#26-11-2014
#Functions starter 1

#calculate basic pay
def calculate_basic_pay(hours,rate):
    total = hours*rate
    return total

#calculate overtime pay
def calculate_overtime_pay(hours,rate):
    overtime_hours = hours-40
    basic_pay = 40*rate
    overtime_pay = overtime_hours*rate*1.5
    total = overtime_pay+basic_pay
    return total

#calculate total pay
def calculate_total_pay(hours,rate):
    if hours <= 40:
        total = calculate_basic_pay(hours,rate)
    else:
        total = calculate_overtime_pay(hours,rate)
    return total

#getting the user to input the hours and rate of pay
def hours_and_rate():
    hours = int(input("Enter the number of hours you work for:"))
    rate = int(input("Enter your rate of pay:"))
    return hours,rate

#displaying the total pay. It has no returned value so there's no need to use return.
def display_total_pay(total):
    print(total)
    
#calculate pay (have to call 3 functions)
def calculate_pay():
    hours,rate = hours_and_rate()
    total = calculate_total_pay(hours,rate)
    display_total_pay(total)
    
calculate_pay()

        




