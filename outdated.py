#implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636, wherein the month in the latter might be any of the values in the list.
#output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in either format, prompt the user again. Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.


def main():
    months = {
        "january": "01",
        "february": "02",
        "march": "03",
        "april": "04",
        "may": "05",
        "june": "06",
        "july": "07",
        "august": "08",
        "september": "09",
        "october": "10",
        "november": "11",
        "december": "12"
    }

    while True:
        user_input = input("Date: ").strip().lower()

        try:
            if "/" in user_input:
                month, day, year = user_input.split("/")
                month = int(month)
                day = int(day)
                year = int(year)
            else:
                split_input = user_input.replace(",", "").split()
                month_name = split_input[0]
                day = int(split_input[1])
                year = int(split_input[2])
                if month_name in months:
                    month = int(months[month_name])
                else:
                    continue

            if not (1 <= int(month) <= 12) or not (1 <= day <= 31):
                continue

            print(f"{year:04}-{int(month):02}-{int(day):02}")
            break

        except (ValueError, IndexError):
            continue


main()
