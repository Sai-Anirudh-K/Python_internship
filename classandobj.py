'''class cse:
    def __init__(self,name,rollno):
        self.n=name
        self.rn=rollno
    def fun(self):
        print("this is a function")
s1=cse('rahul',34)
s2=cse('raghu',36)'''
class cse:
    def __init__(self,name,rollno):
        self.n=name
        self.rn=rollno
    def fun(s):
        print(s.n,s1.rn)
s1=cse('rahul',34)
s2=cse('raghu',36)
s1.fun()
s2.fun()
print(s1.n,s2.n)