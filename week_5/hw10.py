#Cree un programa que le pida al usuario 10 números, 
# y al final le muestre todos los números que ingresó, 
# seguido del numero ingresado más alto.

numbers = []
loops = 10

#loop to request numbers
for i in range(loops):
    user_input = input ("write a number: ")
    if user_input.isdigit():
        number = int(user_input)
        numbers.append(number)
    else:
            print("Not a valid number")

highest = max(numbers)

#Format text for human readablity (I GOOGLED THIS)
readable = ", " .join(str(n) for n in numbers [:-1]) + " and " + str(numbers[-1])

print (f'You enetered {readable}.')
print (f'The highest number is {highest}')
