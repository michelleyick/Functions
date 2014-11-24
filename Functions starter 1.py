#Michelle Yick
#24-11-2014
#Functions starter 1

#calculate total pay
def calculate_basic_pay(hours,rate):
    total = hours*rate
    return total

#calculate overtime pay
def calculate_overtime_pay(hours,rate):
    overtime_hours = hours-40
    basic_pay = overtime_hours*rate*1.5
    total = overtime_pay+basic_pay
    return total

def calculate_total_pay(hours,rate):
    if hours <= 40:
        total = calculate_basic_pay(40,1)
    elif hours > 40:
        total = calculate_overtime_pay(41,1)
    return total
    
        
#main program
total_pay = calculate_basic_pay(12,2)
print(total_pay)

total_

