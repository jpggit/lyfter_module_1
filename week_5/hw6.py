#Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo.
first_list = ["a", "sings", "the"]
second_list = ["bird", "in", "morning"]

#For loop to iterates the len(first_list) times and prints words at indexed positions
for index, word in enumerate(first_list):
    print(first_list[index])
    print(second_list[index])