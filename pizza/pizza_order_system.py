import csv
import datetime

#menüyü ekrana yazdırıyoruz
file = open("menu.txt", "r")
print(file.read())

#Pizza üst sınıfını oluşturuyoruz.
class Pizza:
    def get_description(self): 
        return self.__class__.__name__

    def get_cost(self): 
        return self.__class__.cost 
#Pizza alt sınıflarını oluşturuyoruz.
    def __init__(self):
        self.description = "Unknown Pizza"
    
    def get_description(self):
        return self.description

    def get_cost(self):
        return 0.0

class ClassicPizza(Pizza):
    def __init__(self):
        self.description = "Classic Pizza"
    
    def get_cost(self):
        return 8.99

class MargheritaPizza(Pizza):
    def __init__(self):
        self.description = "Margherita Pizza"
    
    def get_cost(self):
        return 9.99

class PepperoniPizza(Pizza):
    def __init__(self):
        self.description = "Pepperoni Pizza"
    
    def get_cost(self):
        return 10.99
class VegetarianPizza(Pizza):
    def __init__(self):
        self.description = "Vegetarian Pizza"
    
    def get_cost(self):
        return 6.99    

#Decorator üst sınıf oluşturulacak.
class Decorator(Pizza):
    def __init__(self, component):
        self.component = component

    def get_cost(self):
        return self.component.get_cost() + Pizza.get_cost(self)

    def get_description(self):
        return self.component.get_description() + ' ' + Pizza.get_description(self)

#Decorator alt sınıf oluşturulacak 
class Olive(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.description = "Olive"
    
    def get_cost(self):
        return self.component.get_cost() + 1.99

class Mushroom(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.description = "Mushroom"
    
    def get_cost(self):
        return self.component.get_cost() + 2.99

class GoatCheese(Decorator):
    def __init__(self, component):
        Decorator.__init__(self,component)
        self.description = "Goat Cheese" 
    def get_cost(self):
        return self.component.get_cost() + 3.99

class Meat(Decorator):
    def __init__(self,component):
        Decorator.__init__(self,component)
        self.description = "Extra Meat"
    def get_cost(self):
        return self.component.get_cost() + 6.99

class Onion(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.description = "Onion"
    
    def get_cost(self):
        return self.component.get_cost() + 0.99   

class Corn(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.description = "Corn"
    
    def get_cost(self):
        return self.component.get_cost() + 3.99

class NoExtra(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.description = "No Extra"
    
    def get_cost(self):
        return self.component.get_cost() + 0     
               
def main():
    print("Welcome To Pizza House!")
    while True:

     print("Please Choose A Pizza:")
     print("1: Classic")
     print("2: Margherita")
     print("3: Pepperoni")
     print("4: Vegetarian")
     pizza_choice = input("Your Choice: ")

     if pizza_choice == "1":
        pizza = ClassicPizza()
        break
     elif pizza_choice == "2":
        pizza = MargheritaPizza()
        break
     elif pizza_choice == "3":
        pizza = PepperoniPizza()
        break
     elif pizza_choice == "4":
        pizza = VegetarianPizza()
        break
     else:
        print("Invalid Selection, Please Try Again.")      
     
    while True:
     
     print("1: Olive")
     print("2: Mushroom")
     print("3: Goat Cheese")
     print("4: Extra Meat")
     print("5: Onion")
     print("6: Corn")
     print("-: No Extra")
     topping_choice = input("Your Choice: ")
     print

     if topping_choice == "1":
      pizza = Olive(pizza)
      break
     elif topping_choice == "2":
        pizza = Mushroom(pizza)
        break
     elif topping_choice == "3":
        pizza = GoatCheese(pizza)
        break
     elif topping_choice == "4":
        pizza = Meat(pizza)
        break
     elif topping_choice == "5":
        pizza = Onion(pizza)
        break
     elif topping_choice == "6":
        pizza = Corn(pizza)
        break
     elif topping_choice == "-":
         pizza = NoExtra(pizza)
         break
     else:
        print("Invalid Selection, Please Try Again.")

    print("Thanks For Ordering!")
    print("Pizza Cost: $", pizza.get_cost())

#Sipariş Bilgi Kartı oluşturuyoruz.
    print("Order Information")
    name = input("Please Enter Your Name And Surname: ")
    id_number = input("Please Enter Your ID Number: ")
    card_number = input("Please Enter Your Card Number: ")
    card_password = input("Please Enter Your Card Password: ")

    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("Orders_Database.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([pizza.get_description(), name, id_number, card_number, current_time, card_password])
        
if __name__ == "__main__":
    main()