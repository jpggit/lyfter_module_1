#define types of user entry
valid_operators = ['+', '-', '*', '/']
other_actions = ['reset', 'quit']

#BASIC FUNCTIONS -----------------------
#Function to get user input
def get_user_input():
    return input("> ").strip()

#Function to quit
def should_quit(user_input):
    return user_input.lower() == 'quit'

def should_reset(user_input):
    return user_input.lower() == 'reset'

def add(a, b): #suma
    return a + b

def subtract(a, b): #resta
    return a - b 

def multiply(a, b): #multiplicación
    return a * b

def divide(a, b): #división
    if b == 0:
        return 0
    return a / b

#Perform operation
def perform_operation(current, operator, next_number):
    if operator == '+':
        return add(current, next_number)
    elif operator == '-':
        return subtract(current, next_number)
    elif operator == '*':
        return multiply(current, next_number)
    elif operator == '/':
        return divide(current, next_number)
    else:
        print("Invalid operator")
        return current

#Handle if a user enters a number after a number, resetting the oparation
def handle_number_input(number, current, current_operator):
    if current is None:
        return number
    elif current_operator is None:
        return number
    else:
        return current  # current doesn't change yet if we already have operator


#MAIN ------------------------------------
#Run calculator
def run_calculator():
    current = None   
    next_number = None
    current_operator = None

    while True:
        user_input = get_user_input() #Get user input

        if should_quit(user_input): #Check if input = quit
            break

        elif should_reset(user_input): #Check if input = reset
            current, current_operator, next_number = None
            print (f'{current}')
        
        elif user_input in valid_operators: 
            if current is None: #logic to make sure we have a number before an operator
                print ("Enter a number before an operator")
                continue
            else: 
                current_operator = user_input
                print(current_operator)
        
        else: #if its not a quit, reset or operator, then it must be a number
            try:
                number = float(user_input)
                current = handle_number_input(number, current, current_operator)

                if current_operator is not None:
                    next_number = number
                
                    #Now that we have the next number we can perform the operation
                    current = perform_operation(current, current_operator, next_number)
                    
                    print (current)
                    current_operator = None #reset
                    next_number = None #reset

            except ValueError:
                print("Invalid input. Enter a number or an operator.")


run_calculator()