#Number 1: Calculate Days
h1 = eval(input("Enter the hour(s): ")) #input
min1 = eval(input("Enter the minute(s): "))
sec1 = eval(input("Enter the second(s): "))

def convert_to_days():
    global h1, min1, sec1 #function for input, and giving the local variable access to 'h1', 'min1', and 'sec1' global variable
    return (h1, min1, sec1)

def get_days(h1, min1, sec1): #division of hour(s), minute(s), and second(s), for the number of days
    return (h1/24 + min1/1440 + sec1/86400) 

convert_to_days()
print(round(get_days(h1,min1,sec1),4)) #to get value for days and rounding it up to 4 digits after decimal point

#Number 2: Weight on Another Planet
def calc_weight_on_planet(x, grav = 23.1): #default value of Jupiter's surface gravity
    return (x/9.8 * grav) #calculate your weight on Earth in pounds

calc_weight_on_planet()

#Number 3: Atoms
def num_atoms(n, amu = 196.97): #default value of atomic weight of gold
    return ((n/amu) * 6.022 * 10**23) #to calculate the number of atoms: divide its weight in grams by the amu, then multiply the result by Avogadro's number
    
num_atoms()

#Number 4: Aspect Ratio
def keep_aspect_ratio():
    current_width = eval(input('Please Enter Current Width: ')) #input width
    current_height = eval(input('Please Enter Current Height: ')) #input width
    desired_width = eval(input('Please Input Desired Width: ')) #input desired width
    new_height = (desired_width / current_width) * current_height #using ratio to find new height
    print(f'Current Width: {current_width}')
    print(f'Current Width: {current_height}') #printing the current and new width and height
    print(f'New Width: {desired_width}')
    print(f'New Height: {new_height}')

keep_aspect_ratio()

#Number 5: Convert Temperature
fahr = eval(input("Enter the temperature in Fahrenheit: ")) #input

def temp(): #input fahrenheit
    global fahr
    return (print(f"The temperature in Fahrenheit is: {fahr}"))

def celsius(): #calculate celsius
    global fahr
    return (print(f"The temperature in Celsius is: {(fahr - 32) * 5/9}"))

def kelvin(): #calculate kelvin
    global fahr
    return (print(f"The temperature in Kelvin is: {((fahr - 32) * 5/9) + 273.15}"))

temp()
celsius() #printing fahrenheit, celsius, and kelvin
kelvin()