#Michelle Yick
#31-12-2014
#Functions class exercises. Stretch/ challenge. Q1:

#IF m/cm to ft/inches:
def metres_and_centermetres_to_feet_and_inches(metres,centermetres):
    metres_to_inches = metres*39.37
    centermetres_to_feet = centermetres*0.397
    print("Your converted amount is {0} feet and {1} inches".format(centermetres_to_feet,metres_to_inches))

#IF ft/inches to m/cm:
def feet_and_inches_to_metres_and_centermetres(feet,inches):
    feet_to_centermetres = feet*30.48
    inches_to_metres = inches*2.54
    print("Your converted amount is {0} metres and {1} centermetres".format(inches_to_metres,feet_to_centermetres))

#Ask if they want m/cm to ft/inches:
def decision():
    decision = int(input("Would you like to 1.convert from ft/inches to m/cm or 2.convert from m/cm to ft/inches"))
    if decision == 1:
        feet = int(input("Enter the amount of feet"))
        inches = int(input("Enter the amount fo inches"))
        feet_and_inches_to_metres_and_centermetres(feet,inches)
    elif decision == 2:
        metres = int(input("Enter the amount of metres"))
        centermetres = int(input("Enter the amount of centermetres"))
        metres_and_centermetres_to_feet_and_inches(metres,centermetres)
    return metres,centermetres,feet,inches

#Main program:
def converting_measurements():
    feet,inches = decision()
    metres,centermetres = decision()
    feet_and_inches_to_metres_and_centermetres(feet,inches)
    metres_and_centermetres_to_feet_and_inches(metres,centermetres)
converting_measurements()

    
        
