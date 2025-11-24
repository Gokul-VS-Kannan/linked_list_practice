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

    # method to add a node after some node in linked list
    def add_after(self,data,x):
        n = self.head

        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print("Tne node doesnot exist in Linked List")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    # method to add a node before some node in linked list
    def add_before(self,data,x):
        if self.head is None:
            print("Linked list is empty")
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("Node not found in linked list")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    # method to remove head
    def remove_head(self):
        if self.head is None:
            print("Linked list is empty so cant remove head node")
        else:
            self.head = self.head.ref

    # method to remove last node
    def remove_tail(self):
        if self.head is None:
            print("Linked list is empty so cant remove head node")
        elif self.head.ref is None:
            self.head = None
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

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
my_ll.add_after(50,10)
my_ll.show()
my_ll.add_before(30,50)
my_ll.show()

my_ll.remove_head()
my_ll.show()
my_ll.remove_tail()
my_ll.show()