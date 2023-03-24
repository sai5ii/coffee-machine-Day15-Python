from data import MENU, resources
from replit import clear

global overall_income
overall_income = 0

def update_resources(**ingredients):
    """update the resources dict with given ingredients values"""
    for key, value in ingredients.items():          
        resources[key] += value
      
def order_coffee():
    """order the coffe from given menu choices, update inventory 
    accordingly"""
    drink_required = input(
        "What would you like to order: 1.Espresso 2.Latte 3.Cappuccino: "
    ).lower()
    if drink_required in ("espresso","1"):
      ordered_drink = 'espresso'
    elif drink_required in ("latte","2"):
      ordered_drink = 'latte'
    elif drink_required in ("cappuccino","3"):
      ordered_drink = 'cappuccino'
    else:
      clear()
      print("Not a valid choice of drink")
      return

    cost = int(MENU[ordered_drink]['cost'])
    #output the price
    print(f"The price of the {ordered_drink} is ${cost} ")

    #input the money if enough output the coffee , change of user. if not message user not enough money and ask again for option 1
    quarters_inserted = int(input("How many quarters: ")) * 0.25
    dimes_inserted = int(input("How many dimes: ")) * 0.10
    nickels_inserted = int(input("How many nickels: ")) * 0.05
    pennies_inserted = int(input("How many pennies: ")) * 0.01

    total_money = round((quarters_inserted + dimes_inserted +
                         nickels_inserted + pennies_inserted), 2)
    change_avaialbe = round((total_money - cost), 2)
    brew_coffee = False
    out_of_resources = []
    used_inventory = {}
 
    if change_avaialbe < 0:
        print(f"Sorry , not enough money to order {ordered_drink}")
        return

    else:
        for keys, value in MENU[ordered_drink]['ingredients'].items():
            
            if value > resources[keys]:
                out_of_resources.append(keys)
                brew_coffee = False
                break
            else:
                brew_coffee = True
                used_inventory[keys] = value

    if brew_coffee:
        for keys, value in used_inventory.items():
          resources[keys] -= value
        global overall_income
        overall_income += cost
        print(f"Enjoy your warm cup of ☕︎ {ordered_drink}")
        print(f"Here is your change ${change_avaialbe}")
        resources.update({'money': overall_income})
        
    else:
        print(f"Sorry, out of {','.join(out_of_resources)}")


def print_report():
    for keys, value in resources.items():
        print(f"{keys} : {value}")

exit = False

while not exit:
    user_option = input(
        "Select your option 1.Order Coffee, 2. View Reports , 3.Update Inventory, 4.Exit: "
    ).lower()

    if user_option in ("order coffee", "1"):
        clear()
        order_coffee()
    elif user_option in ("view reports", "2"):
        clear()
        print_report()
    elif user_option in ("update_inventory", "3"):
      milk = int(input("How much milk is being delivered: "))  
      water = int(input("How much water is being delivered: "))
      coffee = int(input("How much coffee is being delivered: "))  
      update_resources(water=water,milk=milk,coffee=coffee)
      clear()
      print("Updated inventory..")
      print_report()
    elif user_option in ("exit", "4"):
        exit == True
        clear()
        print("Have a lovely day !! Goodbye")
        break
    else:
        clear()
        print("Not a valid choice")