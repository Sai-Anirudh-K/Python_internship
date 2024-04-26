'''take marks of 5 subjects from a student and calculate percentage.depending on the percentage print grade
more then 75 - grade a
60-74 - b
35-59 - c
less than 34 - fail'''
sub1=int(input())
sub2=int(input())
sub3=int(input())
sub4=int(input())
sub5=int(input())
c=(sub1+sub2+sub3+sub4+sub5)/5           #or (sub1+sub2+sub3+sub4+sub5/500)*100
print(type(c))
if(c>=75):
    print("grade A")
elif(c>=60 and c<=74):
    print("grade B")
elif(c>=35 and c<=59):
    print("grade C")
else:
    print("fail")
                           