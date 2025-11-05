# creating an node
class Node :
    def __init__(self,data):
        self.data = data
        self.pointer = None
    
# creatring class for linked list

class LinkedList :
    def __init__(self):
        self.head = None

    # function to add node
    def add(self,data):
        new = Node(data)
        # check if head node exist or not if no head node then make new node as head
        if self.head is None:
            self.head = new
            return self.head
        # if we have head node then make the new node as the tail
        else:
            current = self.head
            # loop through the linked list untill the pointer reach none
            while current.pointer is not None:
                # make the current as next node
                current = current.pointer
            # once the pointer is none break the loop and link the new node now
            current.pointer = new

