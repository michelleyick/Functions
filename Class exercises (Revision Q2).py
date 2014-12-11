#Michelle Yick
#08-12-2014
#Functions class exercises. Revision Q2

#The base of the pyramid
def pyramid_base(number):
    total = number()
    return total

#Calculate answer(construction of the pyramid). IF the base number entered is odd.
def pyramid_body(number):
    while number%2 == 0:
        number = int(input("Please enter a odd number"))
        total = "*" * ask_for_number()
    return total

#Ask for number:
def ask_for_number():
    number = int(input("Please enter a odd number"))
    return number

#Display pyramid
def display_pyramid(total):
    print(total)

#Main program
def printing_a_pyramid():
    number = ask_for_number()
    total = pyramid_body(number)
    display_pyramid(total)

printing_a_pyramid()
