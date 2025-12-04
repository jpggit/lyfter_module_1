#3. Cree un programa con un numero secreto del 1 al 10. 
# El programa no debe cerrarse hasta que el usuario adivine el numero.
# 1. Debe investigar cómo generar un número aleatorio distinto cada vez que se ejecute.

import random

def generate_random_number():
    return random.randint(1,10)
random_number = generate_random_number()

guess = int(input("Ingrese un número del 1-10: "))

while guess != random_number:
    guess = int(input("Inténtelo de nuevo. Ingrese un número del 1-10: "))

print (f'Correct, el número es {guess}')