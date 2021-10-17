#Forum Task: Fractions and Mixed Numbers

num = eval(input("Enter a numerator that is greater than 0:"))
while num<=0:
    num = eval(input("Please re-enter the numerator. Value must be greater than 0:"))

denom = eval(input("Enter a denominator that is greater than 0:"))
while denom<=0:
    denom = eval(input("Please re-enter the denominator. Value must be greater than 0:"))

import math
GCD = int(math.gcd(num, denom))

if num < denom:
    print (f'{num} / {denom} is a proper fraction.')
    if GCD == 1:
        print ('This proper fraction cannot be reduced any further.')
    else:
        print (f'The proper fraction can be reduced to:')

elif num >= denom:
    print (f'{num} / {denom} is a improper fraction.')
    if GCD == 1:
        print ('This proper fraction cannot be reduced any further.')
    else:
        print (f'The proper fraction can be reduced to:')

    mix = num%denom   
    if mix != 0:
        print ('The mixed number is {mix}')
    else:
        print ('The whole number is {num}')
