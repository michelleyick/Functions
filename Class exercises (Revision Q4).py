#Michelle Yick
#11-12-2014
#Functions class exercises. Revision Q4.

#Do calculation to convert the temperature from fahrenheit to celcius:
def convert_fahrenheit_to_celcius(fahrenheit):
    total = fahrenheit-32
    return total

#INPUT the temperature in fahrenheit:
def input_fahrenheit():
    fahrenheit = int(input("Enter the temperature you want to convert in Fahrenheit:"))
    return fahrenheit

#Display the temperature in celcius:
def display_temperature_in_celcius(total):
    print(total)

#(MAIN PROGRAM) - Converting fahrenheit to celcius:
def fahrenheit_to_celcius():
    fahrenheit = input_fahrenheit()
    total = convert_fahrenheit_to_celcius(fahrenheit)
    display_temperature_in_celcius(total)
fahrenheit_to_celcius()

    
