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

    # method to add after new node
    def add_after(self,data,x):
        if self.head is None:
            print("The linked list is empty")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print("Node not found in the Linked List")
            else:
                new_node = Node(data)
                new_node.nref = n.nref
                new_node.pref = n
                if n.nref is not None:
                    n.nref.pref = new_node 
                n.nref = new_node

    # method to add before
    def add_before(self,data,x):
        if self.head is None:
            print("linked list is empty")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print("Node not found in the Linked List")
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                else:
                    self.head = new_node
                n.pref = new_node

    # method to remove head node
    def remove_head(self):
        if self.head is None:
            print("Linked list is empty")
            return
        if self.head.nref is None:
            self.head = None
        else:
            self.head = self.head.nref
            self.head.pref = None

    # method to remove tail node
    def remove_tail(self):
        if self.head is None:
            print("Linked list is empty")
            return
        if self.head.nref is None:
            self.head = None
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.pref.nref = None

    # method for deleting a node
    def delete(self,x):
        if self.head is None:
            print("Linked list is Empty")
            return
        if self.head.nref is None:
            if x == self.head.data:
                self.head = None
            else:
                print(x," not found in the linked list")
            return
        if x == self.head.data:
            self.head = self.head.nref
            self.head.pref = None
            return
        n = self.head
        while n.nref is not None:
            if n.data == x:
                break
            n = n.nref
        if n.nref is not None:
            n.nref.pref = n.pref
            n.pref.nref = n.nref
        else:
            if x == n.data:
                n.pref.nref = None
            else:
                print(x,"not present in linked list")
        
# creating an instace of linked list
my_dll = doubly_linked_list() 
my_dll.add_empty(100)
my_dll.show()

my_dll.add_begin(50)
my_dll.show()

my_dll.add_end(110)
my_dll.show()

my_dll.show_reverse()

my_dll.add_after(80,50)
my_dll.add_after(90,80)
my_dll.add_after(120,110)
my_dll.show()

my_dll.add_before(70,80)
my_dll.add_before(60,70)
my_dll.add_before(10,50)
my_dll.show()

my_dll.remove_head()
my_dll.show()

my_dll.remove_tail()
my_dll.show()

my_dll.delete(80)
my_dll.delete(50)
my_dll.delete(110)
my_dll.delete(140)
my_dll.show()