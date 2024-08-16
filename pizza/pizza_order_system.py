import csv
import datetime
import re

def luhn_algorithm(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    
    checksum = sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    
    return checksum % 10 == 0

def check_credit_card_number(card_number):
    card_number = card_number.replace(' ', '')
    if not card_number.isdigit():
        return False
    return luhn_algorithm(card_number)

def get_card_type(card_number):
    card_number = card_number.replace(' ', '')
    card_types = {
        "Visa": r"^4[0-9]{12}(?:[0-9]{3})?$",
        "MasterCard": r"^5[1-5][0-9]{14}$",
        "American Express": r"^3[47][0-9]{13}$",
        "Discover": r"^6(?:011|5[0-9]{2})[0-9]{12}$",
        "JCB": r"^(?:2131|1800|35\d{3})\d{11}$",
        "Diners Club": r"^3(?:0[0-5]|[68][0-9])[0-9]{11}$",
        "Maestro": r"^(5018|5020|5038|56|57|58|6304|6759|676[1-3])\d{8,15}$",
        "Verve": r"^(506[01]|507[89]|6500)\d{12,15}$"
    }
    
    for card_type, pattern in card_types.items():
        if re.match(pattern, card_number):
            return card_type
    return "Unknown"

class Pizza:
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

class Decorator(Pizza):
    def __init__(self, component):
        self.component = component

    def get_cost(self):
        return self.component.get_cost() + Pizza.get_cost(self)

    def get_description(self):
        return self.component.get_description() + ' ' + Pizza.get_description(self)

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

    print("Order Information")
    name = input("Please Enter Your Name And Surname: ")
    id_number = input("Please Enter Your ID Number: ")
    
    while True:
        card_number = input("Please Enter Your Card Number: ")
        if check_credit_card_number(card_number):
            card_type = get_card_type(card_number)
            print(f"Card Type: {card_type}")
            break
        else:
            print("Invalid credit card number. Please try again.")
    
    card_password = input("Please Enter Your Card Password: ")

    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("pizza/3Orders_Database.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([pizza.get_description(), name, id_number, card_number, card_type, current_time, card_password])

if __name__ == "__main__":
    main()
