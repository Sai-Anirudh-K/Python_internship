'''take two int input from user and use function to add those two values, function should not contain print statement and has to return
the result'''



def Sum(a:int,b:int)->int:
    c=a+b                                  #or return a+b
    return c
a=int(input())
b=int(input())
print(Sum(a,b))