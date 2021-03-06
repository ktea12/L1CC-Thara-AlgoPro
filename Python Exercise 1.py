#Slope of a line
x1 = eval(input("Enter the x-coordinate for point 1:"))
y1 = eval(input("Enter the y-coordinate for point 1:"))
x2 = eval(input("Enter the x-coordinate for point 2:"))
y2 = eval(input("Enter the y-coordinate for point 2:"))

slope =(y2-y1)/(x2-x1)
formatted_slope = "{:.5f}".format(slope)

print(f'The slope for the line that connects point 1 {x1,y1} and point 2 {x2,y2} is {formatted_slope}')

#Runway Length
v = eval(input("Enter the planes take off speed in m/s:"))
acc = eval(input("Enter the plane's acceleration in m/s**2:"))

runway = v**2/(2*acc)
formatted_runway = "{:.4f}".format(runway)

print(f'The minimum runway length needed for this airplane is {formatted_runway} meters')

#Tip Calculator
sub = eval(input("Enter the subtotal: $"))
gratuity = eval(input("Enter tip amount (as a %):"))

tip = sub*gratuity/100
total = sub + tip
currency = "${:,.2f}".format(sub)
formatted_tip = "${:,.2f}".format(tip)
formatted_total = "${:,.2f}".format(total)

print(f'Subtotal: {currency}')
print(f'Tip: {formatted_tip}')
print(f'Total: {formatted_total}')

#Area of Hexagon
side = eval(input("Enter the side length of the hexagon:"))

import math
area = (3 * math.sqrt(3)/2) * pow(side,2)
formatted_area = "{:.3f}".format(area)

print(f'The area of a hexagon with side length {side} is {formatted_area}')