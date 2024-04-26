'''prime number or not with functions
for i in range(2,n):
    if n%i==0:
        print("not a prime no")
        break
else:
    print("prime no)'''




n=int(input())
def Prime(n)->bool:
    for i in range(2,n):
        if n%i==0:
            flag=True
            return flag
            break
    else:
     flag=False
     return flag
flag=Prime(n)
if flag==True:
    print("not a prime number")
elif flag==False:
    print("prime number")
    
