#Implement a program that prompts the user for the answer to the Great Question of Life, the Universe, and everything.
#If the user inputs 42 Output "Yes" otherwise if the user inputs forty-two or forty two output No

def solution(x):
    if x == "42":
        print("Yes")
    elif x == ("Forty-Two"):
        print("No")
    elif x == ("Forty Two"):
        print("No")
    else:
        print("Incorrect, please try again")


def main():
    user_start = input("What is the answer to the Great Question of Life, the Universe, and Everything? ")
    user_start = solution(user_start)
    return solution 

main()

