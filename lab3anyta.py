# Function 1:
def check_weekday_or_weekend(day):
    if 1<= day <= 5:
        print("It is a weekday!")
    elif day == 6 or day == 7:
       print("It is a weekend!")
    else:
        print("Invalid input, not a proper day number!")

# Function 2:
def get_day_name(day):
    if day == 1:
        print("It is monday!")
    elif day == 2:
        print("It is tuesday!")
    elif day == 3:
        print("It is wednesday!")
    elif day == 4:
        print("It is thursday!")
    elif day == 5:
        print("It is friday!")
    elif day == 6:
        print("It is saturday!")
    elif day == 7:
        print("It is sunday!")
    else:
        print("Invalied input, not a proper day number!")

if __name__ == '__main__':
    day = int(input("Check weekday or weekend(day)"))
    check_weekday_or_weekend(day)
    get_day_name(day)