#This program outputs the user's input in a specified font. I chose "isometric2," which displays the text in a cool, horizontal bubble style.
#Import used : pip install pyfiglet

from pyfiglet import Figlet

def main():
    f = Figlet(font= 'isometric2')
    userinput = input("Input: ")
    output = f.renderText(userinput)
    print(output)
main()
