class Node:
    def __init__(self,data):
        self.data = data
        self.nref = None
        self.pref = None

# creating class for doubly linked list
class doubly_linked_list:
    def __init__(self):
        self.head = None

    # forward traversal method
    def show(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data,"--->", end=" ")
                n = n.nref
            print("None")

    # backward traversal method
    def show_reverse(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(n.data,"--->",end=" ")
                n = n.pref
            print("None")

    # adding an node to empty linked list
    def add_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Sorry the linked list is not empty")

    # adding node at begning
    def add_begin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

    # adding node at end
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n


# creating an instace of linked list
my_dll = doubly_linked_list() 
my_dll.add_empty(100)
my_dll.show()

my_dll.add_begin(90)
my_dll.show()

my_dll.add_end(110)
my_dll.show()

my_dll.show_reverse()