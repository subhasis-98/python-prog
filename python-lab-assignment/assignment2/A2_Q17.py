# Function to get the name of the day from the number
def get_day_name(day_number):
    if day_number == 0:
        return "Sunday"
    elif day_number == 1:
        return "Monday"
    elif day_number == 2:
        return "Tuesday"
    elif day_number == 3:
        return "Wednesday"
    elif day_number == 4:
        return "Thursday"
    elif day_number == 5:
        return "Friday"
    elif day_number == 6:
        return "Saturday"
    else:
        return "Invalid day"

# Prompt the user to enter today's day of the week
today = int(input("Enter today's day (Sunday is 0, Monday is 1, ..., Saturday is 6): "))

# Prompt the user to enter the number of days after today
days_ahead = int(input("Enter the number of days after today: "))

# Calculate the future day
future_day = (today + days_ahead) % 7

# Get the names of the days
today_name = get_day_name(today)
future_day_name = get_day_name(future_day)

# Display the result
# if today_name == "Invalid day":
#     print("Invalid input for today's day.")
# else:
print(f"Today is {today_name} and the future day is {future_day_name}.")
