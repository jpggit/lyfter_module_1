# 2. Cree una estructura de objetos que asemeje un Double Ended Queue.
#    A. Debe incluir los métodos de `push_left` y `push_right` 
# (para agregar nodos al inicio y al final) y 
# `pop_left` y `pop_right` (para quitar nodos al inicio y al final).
#    B. Debe incluir un método para hacer `print` de toda la estructura.

class Node: 
    data: str
    next: "Node"

    def __init__ (self, data, next = None):
        self.data = data
        self.next = next



class Double_Queue:
    head: Node

    def __init__(self, head=None):
        self.head = head

    def print_method(self):
        current_node = self.head
        while current_node is not None:
            print (current_node.data)
            current_node = current_node.next

    def push_left(self, new_left_node):
        new_left_node.next = self.head
        self.head = new_left_node
    
    def push_right(self, new_right_node):
        if self.head is None:
            self.head = new_right_node
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_right_node

    def pop_left(self):
        if self.head is None:
            return None
        popped_left_node = self.head
        self.head = self.head.next
        return popped_left_node.data

    def pop_right(self):
        if self.head is None:
            return None
        
        if self.head.next is None:
            popped = self.head
            self.head = None
            return popped.data

        previous_node = None
        current_node = self.head
        while current_node.next is not None:
            previous_node = current_node
            current_node = current_node.next
        previous_node.next = None
        return current_node.data


dq = Double_Queue()

dq.push_right(Node("B"))
dq.push_left(Node("A"))
dq.push_right(Node("C"))
dq.push_right(Node("D"))

dq.print_method()
# A
# B
# C
# D

print("pop_right:", dq.pop_right())  # D
dq.print_method()
# A B C

print("pop_left:", dq.pop_left())    # A
dq.print_method()
# B C