#Cree un programa que le pida al usuario su nombre, apellido, y edad, 
# y muestre si es un bebé, niño, preadolescente, adolescente, adulto joven, adulto, o adulto mayor.

name = input("Ingrese su primer nombre: ")
last_name = input("Ingrese su apellido: ")
age = int(input("Ingrese su edad: "))

if age <= 2:
    print (f'{name} {last_name} is a baby')
elif age <= 12:
    print (f'{name} {last_name} is a preteen')
elif age <= 19:
    print (f'{name} {last_name} is a teenager')
elif age <= 26:
    print (f'{name} {last_name} is a young adult')
elif age <= 50:
    print (f'{name} {last_name} is an adult')
else:
    print (f'{name} {last_name} is a baby')