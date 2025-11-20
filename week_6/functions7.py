#Cree una función que acepte una lista de números y retorne 
# una lista con los números primos de la misma.
import math

def prime_checker(numbers):
    prime_numbers = []
    for n in numbers: 
        #conditions that exclude numbers:
        if n <= 1:
            continue
        elif n % 2 == 0:
            continue
        #conditions that include numbers:
        elif n == 2:
            prime_numbers.append(n)
        else:
            is_prime = True
            divisor = int(math.sqrt(n))+1
            for i in range (3, divisor, 2):
                if n%i == 0:
                    is_prime = False
            if is_prime:
                    prime_numbers.append(n)
    print (prime_numbers)


example = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_checker(example)