from datetime import datetime

user_input = input("Enter your goal with a deadline separated by a colon : ")
user_input_list = user_input.split(":")

goal = user_input_list[0]
deadline = datetime.strptime(user_input_list[1],"%d.%m.%Y")

print(deadline)

#calculate how many days from now till deadline

now = datetime.now()

time_remaining = deadline-now

hours_remaining = int(time_remaining.total_seconds()/60/60)

print(f"Dear user! Time remaining for your goal: {goal} is {hours_remaining} hours ")