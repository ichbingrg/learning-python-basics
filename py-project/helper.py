days_to_hours = 24
days_to_minutes = 24*60
days_to_seconds = 24*60*60


def days_to_units(num_of_days, conv_unit):
    if conv_unit=="hours":
        return f"{num_of_days} days are {num_of_days * days_to_hours} {conv_unit}"
    elif conv_unit=="minutes":
        return f"{num_of_days} days are {num_of_days * days_to_minutes} {conv_unit}"
    elif conv_unit=="seconds":
        return f"{num_of_days} days are {num_of_days * days_to_seconds} {conv_unit}"
    else:
        return "unsupported unit"


def validate_and_execute(days_unit_dict):
    try:
        days_number = int(days_unit_dict["days"])
        if days_number > 0:
            calculated_value = days_to_units(days_number, days_unit_dict["unit"])
            print(calculated_value)
        elif days_number == 0:
            print("you entered a 0, Please try again with a positive integer")
        else:
            print("It is a negative number, no conversion for you")
    except ValueError:
        print("your input is not valid")

user_input_message = "Enter the number of days and conversion unit(hours/minutes/seconds) : "
