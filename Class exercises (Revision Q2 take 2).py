#Michelle Yick
#12-12-2014
#Functions class exercises. Revision Q2.

#IF number is not odd:
def number_not_odd(number):
    total = input_number()
    return total

#IF number is odd:
def number_is_odd(number):
    count = 0
    for count in range(number):
        total = print ('*' *(number-count-1) + '*' *(2*count+1))
    return total

#INPUT number:
def input_number():
    number = int(input("Please enter a odd number:"))
    while number%2 == 0:
        number = int(input("Please enter a odd number:"))
    total = number
    return number

#Display the pyramid:
def display_inverted_pyramid(total):
    print(total)

#Main program. Printing an inverted pyramid:
def printing_an_inverted_pyramid():
    number = input_number()
    total = number_is_odd(number)
    display_inverted_pyramid(total)
printing_an_inverted_pyramid()
    
    
    
    
