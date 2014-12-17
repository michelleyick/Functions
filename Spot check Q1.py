#Michelle Yick
#15-12-2014
#Functions spot check.Q1.

#Password is too low:
def low_password(password):
    total = print("Password is too short")
    return total
    input_password()

#Password is too high:
def high_password(password):
    total = print("Password is too long")
    return total
    input_password()

#Password is accepted:
def accepted_password(password):
    total = print("Password is accepted")
    return total
    

#IF password is between 8-16 characters long:
def check_password(password):
    if length_of_password(password) > 16 and length_of_password(password)< 8:
        total = accepted_password(password)
    elif length_of_password(password) > 16:
        total = high_password(password)
    elif length_of_password(password) < 8:
        total = low_password(password)
    return total

#Check length of password:
def length_of_password(password):
    total = len(password)
    return total

#INPUT password:
def input_password():
    password = input("Please enter a password in characters:")
    total = length_of_password(password)
        
    return password

#DISPLAY message:
def display_message(total):
    print(total)

#Main program:
def main_program():
    password = input_password()
    total = check_password(password)
    display_message(total)
main_program()
    
                                  
                                  
    
