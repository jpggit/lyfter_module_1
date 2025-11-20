# Cree una función que acepte un string con palabras 
# separadas por un guión y retorne un string igual pero ordenado alfabéticamente.

def alpha_organizer(text):
    words = text.split('-')
    words.sort()
    new_text = '-'.join(words)
    print (new_text)

example_text = "python-variable-funcion-computadora-monitor"
alpha_organizer(example_text)