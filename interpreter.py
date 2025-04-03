#implement a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place
#Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z
#x is an integer, y is +, -, *, or /, and z in an integer
def main():
    user = input("Expression: ")
    splice = user.split()
    x = int(splice[0])
    y = splice[1]
    z = int(splice[2])

    if y == "+":
        final = x + z
    elif y == "-":
        final = x - z
    elif y == "*":
        final = x * z
    elif y == "/":
        final = x / z

    print(f"{final:.1f}")

main()
