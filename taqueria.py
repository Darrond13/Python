#Implement a program that enables a user to place an order, prompting them for items, one per line, until the user inputs control-d 
#After each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign ($) and formatted to two decimal places
#Treat the user’s input case insensitively. Ignore any input that isn’t an item. Assume that every item on the menu will be titlecased.

def main():
    menu_options = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
    Total = 0.0

    while True:
        try:
            user_choice = input("Item: ").strip().title()
            if user_choice in menu_options:
                price = menu_options[user_choice]
                Total += price
                print(f"Total: ${Total:.2f}")
        except EOFError:
                print()
                break

if __name__ =="__main__":
     main()
