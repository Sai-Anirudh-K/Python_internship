try:
    l=[1,2]
    print(l[2])
except:
    print("error")  #will execute only when error is present
finally:
    print("inside")   #will execute whether error is present or not