
from helper import *

user_input = ""

while user_input != "exit":
    user_input = input(user_input_message)
    days_unit = user_input.split(":")
    #print(days_unit)
    days_unit_dict = {"days": int(days_unit[0]), "unit":days_unit[1]}
    #print(days_unit_dict);

    validate_and_execute(days_unit_dict)
