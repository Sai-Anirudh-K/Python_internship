def fun(l,ind):
    try:
        a=l.copy()
        a[0]=l[0]/l[ind]
    except ValueError:
        print("value error")
    finally:
        print("end of func")
l=[1,2,3,4,5]
try:
    fun(l,5)
except IndexError:
    print("index error")
finally:
    print("End of blocks")
raise ValueError("this is a value error")