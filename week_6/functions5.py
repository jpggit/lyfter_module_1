#Cree una función que imprima el 
# numero de mayúsculas y el numero de minúsculas en un string.

def counter(string):
    capitalized = 0
    lower_case = 0
    for char in string:
        if char.isupper():
            capitalized += 1
        elif char.islower():
            lower_case += 1
    
    print (f'There’s {capitalized} upper cases and {lower_case} lower cases')


counter("May the Force be with you")