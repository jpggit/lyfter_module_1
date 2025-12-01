
valid_operators = ['+', '-', '*', '/']
other_actions = ['reset', 'quit']

#A function to collect a NUMBER (float or int)
def get_number_input(prompt):
    while True:
        user_input = input(prompt)
        try:
            return float(user_input)
        except ValueError:
            print (f'{user_input} is not a number. Try again')

#A function to collect the OPERATOR or a reset / quit
def get_operator():
    while True:
        input_operator = input("Enter operator (+, -, *, /) or 'reset' or 'quit': ")
        if input_operator in valid_operators or input_operator in other_actions:
            return input_operator
        else: 
            print ("Invalid operator. Try again")

#Main function to run the calculator
def run_calculator():
    #Get the first number
    current = get_number_input("Enter the first number to start: ")
    print(f"{current}")

    #Loop to get valid operator and next number at infinitum
    while True:
        operator = get_operator()

        if operator == 'quit':
            break

        if operator == 'reset':
            current = get_number_input("Enter a new starting number: ")
            print(f"{current}")
            continue
        
        next_number = get_number_input("Enter nextg number: ")

        if operator == '/' and next_number == 0:
            print("Cannot divide by zero. Try a different number.")
            continue
            

        #CALculation

        if operator == '+':
            current += next_number
        elif operator == '-':
            current -= next_number
        elif operator == '*':
            current *= next_number
        elif operator == '/':
            current /= next_number

        print(f'Result: {current}')

run_calculator()