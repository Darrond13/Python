#implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case. Assume that the user’s input will indeed be in camel case.
def camel_to_snake(name):
    snake_case = ""
    for char in name:
        if char.isupper():
            snake_case += "_" + char.lower()
        else:
            snake_case += char
    return snake_case

def main():
    name = input("camelCase: ")
    print("snake_case: " + camel_to_snake(name))


main()
