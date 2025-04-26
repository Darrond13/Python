#implement a program that prompts the user for a str in English and then outputs the “emojized” version of that str, converting any codes (or aliases) therein to their corresponding emoji.
#pip terminal install I used: python3 -m pip install emoji --break-system-packages
#List of codes with aliases for this program: https://carpedm20.github.io/emoji/all.html?enableList=enable_list_alias
#Example: Hello, :earth_africa:

import emoji 

def main():
    user = input("Input: ")

    convert_emoji = emoji.emojize(user, language='alias')

    print("Output:", convert_emoji) 

main()
