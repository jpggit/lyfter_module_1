#Cree un programa que itere e imprima un string letra por letra de derecha a izquierda.

word = input("Submit a word: ")

for letter in range(len(word) -1, -1, -1):
    print (word[letter])