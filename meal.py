#implement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time. If it’s not time for a meal, don’t output anything at all.
#Assume that the user’s input will be formatted in 24-hour time, such as #:##, or ##:##
#assume that each meal’s time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.
def convert(time):
        x, y = time.split(":")
        hours = float(x)
        mins = float(y) / 60
        return hours + mins

def main():
    user = input("What time is it? ")
    time = convert(user)
    if 7.0 <= time <= 8.0:
        print("breakfast time")
    elif 12.0 <= time <= 13.0:
        print("lunch time")
    elif 18.0 <= time <= 19.0:
        print("dinner time")
    else:
        return

if __name__ == "__main__":
     main()

