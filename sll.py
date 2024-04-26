class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def insertAtBegin(self, data):
        new=node(data)
        if self.head==None:
            self.head=new
            return
        else:
            new.next=self.head
            self.head=new
            #cyclic sll
        self.tail.next=self.head
        self.head.prev=self.tail
    def InsertAtEnd(self,data):
        new=node(data)
        if self.head==None:
            self.head=new
            return
        else:
            i=self.head
            while i.next:
                i=i.next
            i.next=new
            #cyclic sll
        self.tail.next=self.head
        self.head.prev=self.tail
    def printing(self):
        if self.head==None:
            return
        i=self.head
        while i:
            print(i.data)
            i=i.next
s=sll()
s.insertAtBegin(1)
s.InsertAtEnd(2)
s.InsertAtEnd(6)
s.insertAtBegin(8)
s.printing()

