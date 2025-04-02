#Implement a program that prompts the user for a greeting, if the greeting starts with "hello" output $0 
#If the greeting starts with "h" but not "hello" output $20
#Otherwise output $100 for any other input
#Ignore the leading whitespace and treat the users greeting case-insensitively

def money(m):
    if m == "hello":
        print("$0")
    elif m.startswith("h"):
        print("$20")
    else:
        print("$100")

def main():
    user = input("Greeting: ")
    user = user.strip().lower()
    user = money(user)
    return money 

main()
