#Cree un programa que use una lista para eliminar keys de un diccionario.

remove = ['access_level', 'age']
employee = {
    'name': 'John',
    'last name': 'Brenes',
    'access_level': 5,
    'age': 45,
    'job': 'manager',
}

#loop to remove items (i) from the employee dictionary
for index, key in enumerate(remove):
    employee.pop(key)
    print (f'removed {key} at index {index}')

print (employee)