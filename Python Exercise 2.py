#Ramp Angle
mass = eval(input("Enter the mass of the cart (in kg):"))
force = eval(input("Enter the force to push the cart (in N):"))
constant = 9.8

import math
angle = (mass*constant) / force
arcsin = math.asin(1/angle)
degreeangle = math.degrees(arcsin)
formatted_angle = "{:.1f}".format(degreeangle)

print(f'The angle of the ramp is {formatted_angle} degrees')

#Perimeter of a Triangle
edge1 = eval(input("Enter length of edge 1:"))
edge2 = eval(input("Enter length of edge 2:"))
edge3 = eval(input("Enter length of edge 3:"))

if(edge1 + edge2 > edge3 and edge3 + edge2 > edge1 and edge1 + edge3 > edge2):
    print(f'The perimeter is {edge1 + edge2 + edge3}')

else: print('Perimeter cannot be calculated due to invalid input.')

#Wind-Chill Temperature
temp = eval(input("Enter the temperature in Fahrenheit:"))
while -58>temp>41:
    print ('Temperature must be between -58F and 41F')
    temp = eval(input("Please re-enter the temperature in Fahrenheit:"))

speed = eval(input("Enter the wind speed in miles per hour:"))
while speed<2 and speed!=2:
    print ('Speed must be greater than or equal to 2')
    speed = eval(input("Please re-enter the wind speed in miles per hour:"))
 
windchill = 35.74 + 0.6215*temp - 35.75*speed**0.16 + 0.4275*temp*speed**0.16
formatted_windchill = "{:.3f}".format(windchill)

print(f'The wind chill index is {formatted_windchill}')

#Software Sales
pack = eval(input("Enter the number of packages purchased:"))
packprice = 99*pack
disc = 0

if pack<10:
    disc = 0
elif pack > 9 and pack<=20:
    disc = 10
elif pack > 20 and pack <50:
    disc = 20
elif pack > 51 and pack < 100:
    disc = 30
elif pack > 99:
    disc = 40

discprice = packprice*disc/100
total = packprice - discprice
format_discprice = "${:,.2f}".format(discprice)
format_total = "${:,.2f}".format(total)
print(f'Discount Amount @ {disc}% : {format_discprice}')
print(f'Total amount: {format_total}')