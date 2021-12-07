class shopitemQL:
    def __init__(self, name, amount):
        self.fname = name
        self.famount = amount
        self.price = 0
        self.total = 0
    
    def __pricing(self): #private function for the list of fixed prices of the item
        if self.fname == "dry cured iberian ham":
            self.price = 177.8
        elif self.fname == "wagyu steaks":
            self.price = 450
        elif self.fname == "matsutake mushrooms":
            self.price = 272
        elif self.fname == "kopi luwak coffee":
            self.price = 306.5
        elif self.fname == "moose cheese":
            self.price = 487.2
        elif self.fname == "white truffles":
            self.price = 3600
        elif self.fname == "blue fin tuna":
            self.price = 3603
        elif self.fname == "le bonnotte potatoes":
            self.price = 270.81
        else:
            self.price = 0
    
    def total(self): 
        self.__pricing() #calling the fixed price function 
        self.total = self.price * self.famount
        return self.total

#try to add getter and setter
#find other ways to call price list

from import shopitemQL
class shoplistQL:
    def