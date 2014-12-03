#Michelle Yick
#03-12-2014
#Functions class exercises. Revision Q1.

#multiply the character by the integer.
def OutputSymbol_character_and_integer(integer,character):
    total = character*integer
    return total

#get the character and integer.
def character_and_integer_input():
    integer = int(input("Enter a number:"))
    character = input("Enter a character:")
    return integer,character

#display the character the number of times according to the integer entered.
def display_total(total):
    print(total)

#main program.
def test_function_output_symbols():
    integer,character = character_and_integer_input()
    total = OutputSymbol_character_and_integer(integer,character)
    display_total(total)

test_function_output_symbols()


