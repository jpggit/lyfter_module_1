from abc import ABC, abstractmethod

#1. Cree una clase de `BankAccount` que:
#   1. Tenga un atributo de `balance`.
#  2. Tenga un método para ingresar dinero.
#    3. Tengo un método para retirar dinero.
#    
#    Cree otra clase que herede de esta llamada `SavingsAccount` que:
#    
#    1. Tenga un atributo de `min_balance` que se pueda asignar al crearla.
#    2. Arroje un error si al intentar retirar dinero, el retiro haría que el
#  `balance` quede debajo del `min_balance`. Es decir que sí se pueden hacer 
# retiros **siempre y cuando** el `balance` quede arriba del `min_balance`.


class BankAccount():
    def __init__(self):
        self._your_balance = 0

    def balance(self):
        print(f"Your balance is of {self._your_balance}")

    def add_balance(self):
        while True:
            __amount = input("Enter the amount you want to add to your account balance or exit: ")
            if __amount.lower() == "exit":
                print("Action canceled.")
                break
            try:
                __amount = int(__amount)
            except ValueError:
                print("Enter a valid numerical amount or 'exit' to end")
                continue
            else:
                self._your_balance += __amount
                print(f"Your new balance is of {self._your_balance}")
                break

    def substract_balance(self):
        while True:
            __amount = input("Enter the amount you want to extract from your account or 'exit': ")
            if __amount.lower() == "exit":
                print("Action canceled.")
                break
            try: 
                __amount = int(__amount)
            except ValueError:
                print("Enter a valid numerical amount")
                continue
            else:
                if  __amount > self._your_balance:
                    print("You do not have enough funds.")
                else:
                    self._your_balance -= __amount
                    print(f"Your new balance is {self._your_balance}")
                    break


class SavingsAccount(BankAccount):
    def __init__(self, min_balance): 
        BankAccount.__init__(self) #! Esto no estaba en las lecciones, pero sin esto no se puede ver _your_balance
        self.min_balance = min_balance

    def substract_balance(self):
        
        while True: 
            __amount = input ("Enter the amount you want to withdraw or 'exit': ")

            if __amount.lower() == "exit":
                print("Action cancelled")
                break
            
            try:
                __amount = int(__amount)
            except ValueError:
                print("Enter a valid numerical amount")
                continue
            
            if self._your_balance - __amount < self.min_balance:
                print("Withdrawal denied: minimum balance requirement not met.")
                continue
            
            self._your_balance -= __amount
            print(f"Your new balance is {self._your_balance}")
            break

#2. Cree una clase abstracta de `Shape` que:
#    1. Tenga los métodos abstractos de `calculate_perimeter` y `calculate_area`.
#    2. Ahora cree las siguientes clases que hereden de `Shape` 
#       e implementen esos métodos: `Circle`, `Square` y `Rectangle`.
#    3. Cada una de estas necesita los atributos respectivos para poder calcular el área y el perímetro.

class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius
    
    def calculate_area(self):
        return 3.14 * (self.radius ** 2)

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        return self.side * 4
    
    def calculate_area(self):
        return self.side ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_perimeter(self):
        return 2 * (self.width + self.height)
    
    def calculate_area(self):
        return self.width * self.height

#Investigue qué usos se le pueden dar a la herencia multiple y cree un ejemplo.

class CreditCardPayment:
    def pay_with_card(self, amount):
        print(f"Paying {amount} with credit card.")

class PayPalPayment:
    def pay_with_paypal(self, amount):
        print(f"Paying {amount} through PayPal.")

class ApplePayPayment:
    def pay_with_apple_pay(self, amount):
        print(f"Paying {amount} using Apple Pay.")

class Checkout(CreditCardPayment, PayPalPayment, ApplePayPayment):
    pass

#! la clase Checkout adopta varios métodos de pago a través de las clases respectivas