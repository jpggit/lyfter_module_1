#1. Cree una estructura de objetos que asemeje un Stack.
# A. Debe incluir los métodos de `push` (para agregar nodos) y 
# `pop` (para quitar nodos).
#B. Debe incluir un método para hacer `print` de toda la estructura.
#C. No se permite el uso de tipos de datos compuestos 
# como `lists`, `dicts` o `tuples` ni módulos como `collections`.


class Node: 
    data: str
    next: "Node"

    def __init__ (self, data, next = None):
        self.data = data
        self.next = next


class Stack:
    head: Node

    def __init__(self, head=None):
        self.head = head

    def print_method(self):
        current_node = self.head
        while current_node is not None:
            print (current_node.data)
            current_node = current_node.next

    def push(self, new_node):
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is None: 
            return None
        popped_node = self.head
        self.head = self.head.next
        return popped_node.data