#Cree un programa que intercambie el primer y ultimo elemento de una lista. 
# Debe funcionar con listas de cualquier tamaño.

my_list = [1, 2, 3, 4, 5, 6]

#Save stuff we will pop out
new_last = my_list[0]
new_first = my_list[-1]

#loop to remove items
indexes_to_remove = [0, -1]
for i in indexes_to_remove:
    my_list.pop(i)

#insertar los elementos guardados en order alterno
my_list.insert(0, new_first)
my_list.insert(-1, new_last)

print (my_list)