#Michelle Yick
#07-12-2014
#Functions class exercises. Task 2.

#Pick out the useful information needed for the personalised message.
def full_name_and_title(title,first,last):
    total = title,first,last
    return total

#Get the information for when the user first signs up.
def information():
    title = input("Enter you title (Mr,Ms,Mrs or Miss):")
    first = input("Enter your first name:")
    last = input("Please enter your last name:")
    t = input("What is the name of the town you live in?:")
    pc = input("Enter your post code")
    street = input("What is the name of the street that you live on?")
    return title,first,last

#Print out the personalised message.
def message(total):
    message = full_name_and_title
    print("Welcome {0}.{1} {2}. Your form has been processed and your registration has been successful".format(title,first,last))
