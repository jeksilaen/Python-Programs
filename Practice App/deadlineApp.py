from _datetime import datetime

user_input = input("Enter your task and the deadline! \n (ex -> Homework : 20/05/2021) : ")
user_input_list = user_input.split(" : ")

task = user_input_list[0]
deadline = user_input_list[1]

deadline_date = datetime.strptime(deadline, "%d/%m/%Y")
today_date = datetime.today()
time_till = deadline_date - today_date

days_difference = time_till.days
hours_difference = time_till.total_seconds()

print(f"Remaining time until \"{task}\" is {time_till} hours")
print(f"Remaining time until \"{task}\" is {days_difference} days")
print(f"Remaining time until \"{task}\" is {int(hours_difference/60/60)} hours")
