#Michelle Yick
#10-12-2014
#Functions class exercises. Revision Q3.

#If x is smaller than y:
def x_is_smaller_than_y(x,y):
    total = y,x
    return total

#If x is greater than y:
def x_is_greater_than_y(x,y):
    total = x,y
    return total

#IF statement. If x is smaller than y:
def if_x_is_smaller_than_y(x,y):
    if x < y:
        total = x_is_smaller_than_y(x,y)
    elif x > y:
        total = x_is_greater_than_y(x,y)
    return total

#Get input values of x and y:
def input_values_of_x_and_y():
    x = int(input("Please enter a value to represent x:"))
    y = int(input("Please enter a value to represent y:"))
    return x,y

#Display x and y in ascending order:
def display_total(total):
    print(total)

#Main program:
def main_program():
    x,y = input_values_of_x_and_y()
    total = if_x_is_smaller_than_y(x,y)
    display_total(total)
main_program()



