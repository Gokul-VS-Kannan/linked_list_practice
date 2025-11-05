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

    # function to display the linked list
    def show(self):
        current = self.head
        # check if head is none or not
        if current is None:
            print("The linked list is empty")
        else:
            # loop and print nodes
            while current is not None:
                print(current.data,end="->")
                # append the current
                current = current.pointer
            print()
    # function to delete node from linked list
    def delete(self,data):
        # check if head is not none
        if self.head is not None:
            # check if value match with the value of head
            if self.head.data == data:
                # shift the head to next node
                self.head = self.head.pointer
            # if value doesnot match
            else:
                current = self.head
                # loop though the linked list untill pointer becomes none and data is not found
                while current.pointer is not None and current.pointer.data != data:
                    # update the current
                    current = current.pointer
                if current.pointer is not None:
                    current.pointer = current.pointer.pointer
                else:
                    print(data,"not found in linked list")
        else:
            print("Linked list is empty")



