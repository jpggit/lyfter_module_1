#1. Cree un decorador que haga print de los parámetros y retorno de la función que decore.
def hw(func):
    def wrapper(*args, **kwargs):
        print (f"Parameters: {args} | {kwargs}")
        result = func(*args, **kwargs)
        print (f"Return value: {result}")
        return result
    return wrapper


#2. Cree un decorador que se encargue de revisar si todos los parámetros de la función 
#    que decore son números, y arroje una excepción de no ser así.

def num_check(func):
    def wrapper (*args, **kwargs):
        for a in args:
            try :
                isinstance(a, (int, float)) #isinstance is a built-in method of Python!
                print(f"{a} is a number")
            except ValueError:
                print(f"{a} is not a number")

        result = func(*args, **kwargs)
        return result
    return wrapper


#3. Cree una clase de `User` que:
#    - Tenga un atributo de `date_of_birth`.
#    - Tenga un property de `age`.
# 
# Luego cree un decorador para funciones que acepten un `User` como parámetro 
# que se encargue de revisar si el `User` es mayor de edad y arroje una excepción de no ser así.

from datetime import date

class User:
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year

        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1

        return age

#--------------
#Decorator 
#--------------
def require_adult(func):
    def wrapper(user, *args, **kwargs):
        if user.age < 18:
            raise Exception("User is not an adult")
        return func(user, *args, **kwargs)
    return wrapper