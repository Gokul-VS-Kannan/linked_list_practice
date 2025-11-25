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