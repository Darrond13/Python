#implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
def main():
    prompt = input("Input: ")
    result = ""
    for c in prompt:
        if c.lower() not in "aeiou":
            result += c
    print(f"Output: ", result)

main()
