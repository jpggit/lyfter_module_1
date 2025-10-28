#Cree un programa que le pida tres números al usuario y muestre el mayor.
number_1 = int(input("Ingrese el primer número: "))
number_2 = int(input("Ingrese el segundo número: "))
number_3 = int(input("Ingrese el tercer número: "))

def mayor (a, b, c):
    return max(a, b, c)

print(mayor(number_1, number_2, number_3))