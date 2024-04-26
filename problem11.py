'''reversing sll and dll

class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def rev(self):
        prev=None
        curr=self.head
        nxt=self.head.next
        while curr:
            if curr.next==None:
                self.head=curr
            curr.next=prev
            prev=curr
            curr=next
        if nxt:
            nxt=nxt.next 
        self.head=prev '''
def reverse(self):    #doubly linked list
    curr=self.head
    while curr:
        if curr.next==None:
           curr.next,curr.prev=curr.prev,curr.next
           curr=curr.prev
    def delatbeg(self,a):
        self.head=self.head.next
        self.head.prev=None
    def delatend(self):
        self.tail=self.tail.prev
        self.tail.next=None
    def delatend(self):                                              #sll
        i=self.head
        while i.next.next:
            i=i.next
        i.next=None  
    
  