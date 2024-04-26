class node:
    def __init__(self,data):
        self.next=None
class sll:
    def __init__(self)->None:
        self.head=None
    def insertatbeg(self,data):
        if self.head==None:
            self.head=node(data)
        else:
            new=node(data)
            new.next=self.head
            self.head=new
    def printing(self):
        if self.head==None:
            return
        i=self.head
        while i:           #i==None i: indicates
            print(i.data)
            i=i.next
    def insertatrear(self,data):
        if self.head==None:
            self.head=node(data)
        else:
            new=node(data)
            i=self.head
            while i.next:
                i=i.next
            i.next=new   
    def length(self):
        count=0
        i=self.head
        while i:
            count+=1
            i=i.next
        return count     

l=[1,2,3,4,5]
o=sll()
for i in l:
    o.insertatrear(i)
o.printing()
