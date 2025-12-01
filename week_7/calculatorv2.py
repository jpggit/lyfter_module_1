#define types of user entry
valid_operators = ['+', '-', '*', '/']
other_actions = ['reset', 'quit']

#take user entry
def run_calculator():
    current = None
    current_operator = None
    next_number = None

    while True:
        user_input = input("> ").strip() #Get input from user

        if user_input.lower() == 'quit': 
            break

        elif user_input.lower() == 'reset':
            current = None
            current_operator = None
            next_number = None
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
                number = float(user_input) #turn input to a float

                if current is None: #if no number has been added, then overwrite it
                    current = number

                elif current_operator is None: #if operator has not been set, overwrite the current
                    current = number
                
                else:
                    next_number = number
                    #Now that we have the next number we can perform the operation
                    if current_operator == '+':
                        current += next_number
                    elif current_operator == '-':
                        current -= next_number
                    elif current_operator == '*':
                        current *= next_number
                    elif current_operator == '/':
                        if next_number == 0:
                            current = 0
                        current /= next_number
                    
                    print (current)
                    current_operator = None #reset
                    next_number = None #reset

            except ValueError:
                print("Invalid input. Enter a number or an operator.")


run_calculator()