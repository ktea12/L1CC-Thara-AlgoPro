#Forum Task Fractions

num = eval(input("Enter a numerator that is greater than 0: "))
while num<=0:
    num = eval(input("Please re-enter the numerator. Value must be greater than 0: "))

denom = eval(input("Enter a denominator that is greater than 0: "))
while denom<=0:
    denom = eval(input("Please re-enter the denominator. Value must be greater than 0: "))


import math
GCD = math.gcd(num, denom)
renum = int(num/GCD)
redenom = int(denom/GCD)

if num < denom:
    print (f'{num} / {denom} is a proper fraction.')
    if GCD == 1:
        print ('This proper fraction cannot be reduced any further.')
    else:
       print (f'The proper fraction can be reduced to: {renum} / {redenom}')

elif num >= denom:
    print (f'{num} / {denom} is a improper fraction.')
    if GCD == 1:
        print ('This proper fraction cannot be reduced any further.')
    else:
        print (f'The proper fraction can be reduced to: {renum} / {redenom}')
    
    
    mix = num // denom
    remain = (renum)%(redenom)   
    if remain != 0:
        print (f'The mixed number is {mix} and {remain} / {redenom}')
    else:
        print (f'The whole number is {renum}')