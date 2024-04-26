class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
        self.tail=None
    def insertAtBeg(self,data):
        new=node(data)
        if self.head==None:
            self.head=new
            self.tail=self.head
        else:
            new.next=self.head
            self.head.prev=new
            self.head=new
    def insertAtEnd(self,data):
        new=node(data)
        if self.head==None:
            self.head=new
            self.tail=self.head
        else:
            self.tail.next=new
            new.prev=self.tail
            self.tail=new
    def printing(self):
        i=self.head
        while i:
            print(i.data)
            i=i.next
o=dll()
for i in range(0,10):
    o.insertAtBeg(i)
o.printing()

