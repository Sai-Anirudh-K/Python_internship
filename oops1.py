#single inheritance

class a:
    branch="cse"      #static variable
    def fun1(self):
        print("fun1")
    def fun2(self):
        print("fun2")
class b(a):           #inheritence
    def fun3(self):
        print("fun3")
    def fun4(self):
        print("fun4")
class c(a,b):               #multiple inheritence
    def fun(self):
        pass
    