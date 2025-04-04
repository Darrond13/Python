#implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty.
#If 99% or more remains, output F instead to indicate that the tank is essentially full
#Be sure to catch any exceptions like ValueError or ZeroDivisionError.

def main():
    while True:
        user_fraction = input("Fraction: ")
        try:
            x_spl, y_spl = user_fraction.split("/")

            x = int(x_spl)
            y = int(y_spl)

            if y == 0 or x > y:
                continue

            ratio = x / y
            percentage = round(ratio * 100)

        except (ValueError, ZeroDivisionError):
            continue

        if percentage <= 1:
            print("E")
        elif percentage >= 99:
            print("F")
        else:
            print(f"{percentage}%")
        break


main()
