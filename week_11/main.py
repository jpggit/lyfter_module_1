
#----------------------------
# Class for Circle
#----------------------------
class Circle:
    def __init__(self, radius): #Attribute
        self.radius = radius
    
    def get_area(self): #Method
        area = round(self.radius**2*3.14, 2)
        return area


#----------------------------
# Class for person
#----------------------------
class Person():
    def __init__(self, name):
        print(f"Ha nacido una persona llamada {name}!")
        self.name = name
        self.age = 0


#----------------------------
# Class for bus - with methods to add and remove people
#----------------------------
class Bus: 
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []  # List to store Person instances

    def add_person(self, person):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
            print(f"{person.name} has entered the bus.")
        else:
            print("The bus is full! No passengers fit.")

    def remove_person(self, person):
        if person in self.passengers:
            self.passengers.remove(person)
            print(f"{person.name} has left the bus.")
        else:
            print(f"{person.name} is not on the bus.")


#----------------------------
# Define each body part
#----------------------------

class Head:
    def __init__(self): #Attributes
        self.eyes = 2
        self.mouth = 1
        self.ears = 2
        self.hair = True
    
    def think(self): #Method
        print ("Thinking...")

class Hand:
    def __init__(self): #Attributes
        self.fingers = 5
    
    def wave(self): #Method
        print("Waving!")

class Arm:
    def __init__(self, hand): #Attributes
        self.hand = hand
    
    def lift(self): #Method
        print("Lifting my arm!")

class Leg:
    def __init__(self, foot): #Attributes
        self.foot = foot
    
    def walk(self): #Method
        print("Walking...")

class Foot:
    def __init__(self): #Attributes
        self.toes = 5
    
    def kick(self): #Method
        print("Kicking!")

class Torso:
    def __init__(self, head, right_arm, left_arm, right_leg, left_leg): #Attributes
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg
    
    def breathe(self): #Method
        print("Breathing...")


#----------------------------
# Now put it into a human
#----------------------------

class Human: 
    def __init__ (self):
        head = Head()
        right_hand = Hand()
        left_hand = Hand()
        right_arm = Arm(right_hand)
        left_arm = Arm(left_hand)
        right_foot = Foot()
        left_foot = Foot()
        right_leg = Leg(right_foot)
        left_leg = Leg(left_foot)

        self.torso = Torso(head, right_arm, left_arm, right_leg, left_leg)
