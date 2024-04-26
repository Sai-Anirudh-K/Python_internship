a=int(input())
'''if a%4==0:
    if a%100==0:
        if a%400==0:
            print("leap year")
        else:
            print("not leap year")
    else:
        print("leap year")
else:
    print("not leap year")'''
if a%100==0 and a%400==0:
    print("leap year")
elif a%100!=0 and a%4==0:
    print("leap year")
else:
    print("not leap year")
