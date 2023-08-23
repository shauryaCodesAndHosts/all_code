class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class doubly_linked_list:
    def __init__(self):
        self.head = None
        self.last = None

    def insert_end(data):
        newNode=Node(data)
        newNode.prev = self.last
        if self.head==None :
            self.next=None
            self.prev=None
        else :
            self.last.next=newNode
            self.last =newNode
    def delete_end(self):
        if self.head !=None:
            if self.head == self.last:
                self.head==None
                self.last==None
            else:
                self.last=self.last.prev
                self.last.ext=None

        

