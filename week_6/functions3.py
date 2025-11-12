#3. Cree una función que retorne la suma de todos los números de una lista.
#    1. La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).
#    2. [4, 6, 2, 29] → 41

def addition(numbers):
    total = sum(numbers)
    return total

#example
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(addition(list))