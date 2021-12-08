from OOPforum3 import shopitemQL

def shoplistQL():
    shoplist = [] #creating an empty list
    
    while True:
        itemnum = eval(input("How many items will you order? ")) #input on how many items will be ordered
        if itemnum < 1: #to make sure the user will input atleast 1 item
            print("You must order atleast 1 item.")
        else:
            break #break code if user inputs correctly (more or equal to 1 item)
    
    for i in range(itemnum): #will loop the amount of times accordingly to the user's input on how many items they will order
        while True: #keeps the user to prompt atleast more than 0 pounds and the correct item name
            foodname = input("Enter the name of the food: ")
            amount = eval(input("Enter the amount of food in pounds: "))
            item = shopitemQL(foodname, amount)
            if foodname == "" or item.get_price() == 0: #check if the food name is blank and calls .getprice to check if the item is part of the inventory by checking the price
                print("This item is not within the list of food items.\nYou need to enter a valid name.")
            elif amount < 0: #check if pounds is less than 0
                print("The amount you're purchasing must be larger than 0 pounds.")
            else:
                break
        shoplist.append(item) #adds item object to the shopping list created earlier
    
    return shoplist

def display(itemlist):
    print("Here's a summary of the items that you purchased: ")
    print("-" * 50) #decorative purposes
    for i in range(len(itemlist)): #prints out the item details within the list
        print(f"Item #{i + 1}")
        print(itemlist[i].__str__() + "\n")

def calculate_amount(itemlist): #calculate all the subtotal of all the items purchased
    total = 0
    for i in range(len(itemlist)): #it loops through each item object and accumulates the total price
        total += itemlist[i].total()
    return total

shoplist = shoplistQL()
display(shoplist)
print(f"Total Cost: ${calculate_amount(shoplist):.2f}") #formatting what the program will return and the price into 2 decimal points