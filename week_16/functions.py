import math

#function3
def addition(numbers):
    total = sum(numbers)
    return total


#function 4
def reverse(string):
    return string[::-1]

print(reverse('hello'))


#function 5
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

#function 6
def alpha_organizer(text):
    words = text.split('-')
    words.sort()
    new_text = '-'.join(words)
    print (new_text)

example_text = "python-variable-funcion-computadora-monitor"
alpha_organizer(example_text)

#function 7

def prime_checker(numbers):
    prime_numbers = []
    for n in numbers: 
        #conditions that exclude numbers:
        if n <= 1:
            continue
        elif n % 2 == 0:
            continue
        #conditions that include numbers:
        elif n == 2:
            prime_numbers.append(n)
        else:
            is_prime = True
            divisor = int(math.sqrt(n))+1
            for i in range (3, divisor, 2):
                if n%i == 0:
                    is_prime = False
            if is_prime:
                    prime_numbers.append(n)
    print (prime_numbers)


example = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_checker(example)
