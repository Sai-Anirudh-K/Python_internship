l=[2,3,5,46,4,39,44]
si=0
li=len(l)-1
se=3
while si<=li:
    mid=(si+li)//2
    if l[mid]==se:
        print("ele found")
        break
    elif se>l[mid]:
        si=mid+1
    else:
        li=mid-1
else:
    print("ele not found")

    '''   1.n/2=n/2^1
                  2.n/2/2=n/4=n/2^2
                  3.n/2^3
                  4.n/2^4
                  ......
                  k.n/2^k=1
                  n=2^k
                  log2(n)=log2(2^k)
                  log2(n)=k log2(2)
                  k=log2(n)

                  log(n)lee'''