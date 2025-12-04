def login(func):
    def wrapper():
        print (f"Calling function {func.__name__}")
        result = func()
        print (f"Finished function {func.__name__}")
        return result
    return wrapper

@login 
def say_hello():
    print("Hello!")



def debug(func):
    def wrapper(*args, **kwargs):
        print (f"Received function name: {func.__name__}, with arguments: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print (f"{func.__name__} returned {result}")
        return result
    return wrapper

@debug
def add (a, b):
    return a + b

@debug
def multiply (x, y, z=1):
    return x*y*z

add (10, 20)

multiply (3, 2, z=10)
