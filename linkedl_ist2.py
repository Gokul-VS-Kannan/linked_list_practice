class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class linked_list:
    def __init__(self):
        self.head = None

    # method to make a node at head
    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    # method to add a node at end
    def add_end(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    # method to print linked list
    def show(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data,end="--->")
                n = n.ref
            print("None")



# creating objects for linked list
my_ll = linked_list()

my_ll.add_begin(10)
my_ll.add_end(100)
my_ll.add_begin(20)
my_ll.show()
my_ll.add_end(500)
my_ll.show()