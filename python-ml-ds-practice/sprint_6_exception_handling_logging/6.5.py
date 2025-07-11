def day_of_week(day):
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    try:
        return days.get(int(day), "There is no such day of the week! Please try again.")
    except ValueError:
        return "You did not enter a number! Please try again."


print(day_of_week("9"))
