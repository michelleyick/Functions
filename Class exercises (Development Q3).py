#Michelle Yick
#24-12-2014
#Functions class exercises. Development Q3.

#Ask the user for the inputs and what they are:
def input_currency():
    currency = int(input("Please input: 1 for £/$, 2 for £/€ or 3 for €/$")
    if currency == 1: #£/$
        type_con = input("a = £ to $ and b = $ to £")
                   if type_con = a:
                       pounds = int(input("Enter the amount of £'s you wish to convert"))
                   elif type_con = b:
                       dollars = int(input("Enter the amound of $'s you wish to convert"))
    elif currency == 2: #£/€
        type_con = input("c = £ to € and d = € to £")
                   if type_con = c:
                      pounds = int(input("Enter the amount of £'s you wish to convert"))
                   elif type_con = d:
                       euros = int(input("Enter the amount of €'s you wish to convert"))
    elif currency == 3: #€/$
        type_con = input("e = € to $ and f = $ to €")
                   if type_con = e:
                        euros = int(input("Enter the amount of €'s you wish to convert"))
                   elif type_con = f:
                        dollars = int(input("Enter the amound of $'s you wish to convert"))
    return dollars,pounds,euros

                   


        
                
        
                   
