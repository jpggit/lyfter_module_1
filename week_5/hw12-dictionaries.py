#Cree un programa que cree un diccionario usando dos listas 
# del mismo tamaño, usando una para sus keys, y la otra para sus values.

dict = {} #crear diccionario vacío
list_a = ['make', 'model', 'year']
list_b = ['honda', 's800', 1967]

#loop que itera = len(lista)
for i in range(len(list_a)):
    dict[list_a[i]] = list_b[i] #agregar items al diccionario

print (dict)

