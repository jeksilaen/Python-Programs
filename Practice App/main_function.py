def days_to_units(days, units):
    if units == "hours":
        print(f"{days} days are {days * 24} hours")
    elif units == "minutes":
        print(f"{days} days are {days * 24 * 60} minutes")
    else:
        print("Unsupported unit of calculation ")


def validation(my_dictionary):
    try:
        days = int(my_dictionary["days"])
        if days > 0:
            days_to_units(days, my_dictionary["unit"])
        elif days == 0:
            print(f"\"{days}\" is a Zero input, please select a positive number!!")
        else:
            print(f"\"{days}\" is a Negative input, please select a positive number!")
    except ValueError:
        print("Invalid input!")


user_input_msg = "Enter a number of days and the conversion unit : "
user_validation_msg = "Do you want to exit the application (yes/no) ?"
