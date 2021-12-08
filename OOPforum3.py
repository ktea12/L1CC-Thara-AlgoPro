class shopitemQL: #create class for shopping items

    import math #import math to be used in calculations 

    def __init__(self, name, amount): #getter function, getting values: name of food, and its amount
        self.foodn = name #food name
        self.foodamt = amount #food amount
        self.price = 0 #defaulting price to 0
        self.ptotal = 0 #defaulting total price to 0
    
    def __pricing(self): #private function to give the food items fixed prices
        if self.foodn.upper() == "DRY CURED IBERIAN HAM": #turning all the string input to upper case so the program can check whether or not item is in the list and has a fixed price
            self.price = 177.8
        elif self.foodn.upper() == "WAGYU STEAKS":
            self.price = 450
        elif self.foodn.upper() == "MATSUTAKE MUSHROOMS":
            self.price = 272
        elif self.foodn.upper() == "KOPI LUWAK COFFEE":
            self.price = 306.5
        elif self.foodn.upper() == "MOOSE CHEESE":
            self.price = 487.2
        elif self.foodn.upper() == "WHITE TRUFFLES":
            self.price = 3600
        elif self.foodn.upper() == "BLUE FIN TUNA":
            self.price = 3603
        elif self.foodn.upper() == "LE BONNOTTE POTATOES":
            self.price = 270.81
        else: #anything outside of the menu will have the value of 0 so it will not be calculated
            self.price = 0
    
    def get_price(self): #to get and apply the fixed price amount on self.price for the driver
        self.__pricing()
        return self.price

    def total(self):
        self.__pricing() #calling the fixed price function from private pricing function
        self.ptotal = self.price * self.foodamt #total price calculation of each item, formula is price of food times its amount
        return self.ptotal #to return the total price calculated
    
    def __str__(self) -> str: #setter function needed for private function, setting values
        self.total() #calling the total function
        return (f"Item Name: {self.foodn}\n Amount ordered: {self.foodamt:.1f} pounds\n Price per pound: ${self.price:.2f}\n Price of order: ${self.ptotal:.2f}")
        #formatting what the program will return, also formatting the pounds and price into decimal
