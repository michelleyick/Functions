#Michelle Yick
#08-12-2014
#Functions class exercises. Revision Q2

#The construction for the pyramid
def pyramid_base(number):
    total = number()
    return total

#Calculate answer(construction of the pyramid)
def pyramid_body(number):
    body = number()-2
    return body

#Get number
def number():
    number = int(input("Please enter a odd number"))
    return number

#Display pyramid
def display_pyramid(total,body):
    print(total,body)

#Main program
def printing_a_pyramid():
    total = pyramid_base(number)
    total = pyramid_body(number)
    display_pyramid(total,body)
printing_a_pyramid()
    
    
