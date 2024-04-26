l=[2,3,4,5,6,4]
print(l.append(8))
print(l.extend([2,3,4]))
print(l.insert(1,10))
print(l.pop(3))
print(l.remove(4))
l.clear()   #doesnot delete list but makes list empty
l.sort()     #makes changes to list
sorted(l)   #does not make changes to list
l=['abc','a','ldls']
l.sort(key=len)
print(l)
l=[[2,3,4],[4,5,6],[2,3]]
l.sort(key=lambda a:a[-1])
max(l)
min(l)
print(max(l,key=lambda a:a[-1]))
a=[1,2,3,4]
b=a.copy()
b[0]=5
print(a)
