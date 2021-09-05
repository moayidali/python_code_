
cal_to_unit= 24
unit= "hours"

def days_to_units(num_of_days):
    
        return f"{num_of_days} days are {num_of_days*cal_to_unit} {unit}"
    

def validate_execute():
    try:
        user_input_num = int(num_of_days_element)
        # we want to do conversion only for positive integers
        if user_input_num > 0:
            cal_value = days_to_units(user_input_num)
            print(cal_value)
        elif user_input_num == 0:
            print("your entered 0, please enter +ve number")
        else:
            print("you entered a -ve num, plz enterend positive")
    except ValueError:
        print("your input is not valid number")

user_input = ""
while user_input != "exit":

    user_input = input("Enter the valuse of days as a comma separated list, It will convert into hours\n")
    print(type(user_input.split(",")))
    print(user_input.split(", "))
    for num_of_days_element in user_input.split(","):
        validate_execute()

