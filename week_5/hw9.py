#Cree un programa que elimine todos los números impares de una lista.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
final_list = []

#loop to check if element is od
for i in my_list:
    if i % 2 == 0: 
        final_list.append(i) #append to new list

print (final_list)



