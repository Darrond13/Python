#Write a program that changes ":) --> 🙂" and ":( ---> 🙁)"

def convert(x):
    x = x.replace(":)", "🙂")
    x = x.replace(":(", "🙁")
    return x 

def main():
    user = input("Please type a word followed by a smiley face or sad face, describing that word. ")
    result = convert(user)
    print(result)
main() 