
# Creamos la clase NODO
class node:

    def __init__(self, _data=None, next=None):
        self.data = _data
        self.next = next


# Creamos la clase List
class List:
    def __init__(self):
        self.head = None

    # Método para agregar elementos al inicio
    def add_at_front(self, data):
        self.head = node(data, next=self.head)

    # Método para verificar si la estructura de datos esta vacia
    def is_empty(self):
        return self.head == None

    # Método para agregar elementos al final
    def add_at_end(self, data):
        if not self.head:
            self.head = node(data=data)
            return
        curr = self.headadd_at
        while curr.next:
            curr = curr.next
        curr.next = node(data=data)

    # Método para eleminar nodos
    def delete_node(self, key):
        curr = self.head
        prev = None
        while curr and curr.data.code != key:
            prev = curr
            curr = curr.next
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None

    # Método para obtener el ultimo nodo
    def get_last_node(self):
        temp = self.head
        while (temp.next is not None):
            temp = temp.next
        return temp.data

    # Método para imprimir la lista de nodos
    def print_list(self):
        node = self.head
        while node != None:
            print("[", node.data.code, "]", end=" => ")
            node = node.next

    def getHead(self):
        return self.head