#Michelle Yick
#17-12-2014
#Functions spot check. Q1 second try

#Get the input password of the user:
def get_password():
    password = input("Please enter a password:")
    return password

#Check if the password is the correct length:
def validate_password(password):
    valid = False
    length = len(password)
    if 8 <= length <= 20:
        print("Password accepted")
        valid = True
    elif length < 8:
        print("Password is too short")
    elif length > 20:
        print("Password it too long")
    return valid

#Main program:
def check_password():
    valid = False
    while valid == False:
        password = get_password()
        valid = validate_password(password)
check_password()


