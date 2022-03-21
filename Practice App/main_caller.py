from main_function import validation, user_input_msg, user_validation_msg


cond = False
while not cond:
    user_input = input(user_input_msg)
    user_input_list = user_input.split(" : ")
    my_dictionary = {"days": user_input_list[0], "unit": user_input_list[1]}
    validation(my_dictionary)

    cond2 = False
    while not cond2:
        stop = input(user_validation_msg)
        if stop == "yes" or stop == "Yes":
            print("Thanks!, goodbye :(")
            cond = True
            cond2 = True
        elif stop == "no" or stop == "No":
            print("Lets keep going !")
            cond2 = True
        else:
            print("Please select (yes/no)")
