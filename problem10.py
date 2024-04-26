'''define a class royal enfield and have constructor take values for model_name,colour and mileage. Also,create 3 objects for this class and print
all three properties of objects outside the class(print function should be outside the class )'''

class royalenfield:
    def __init__(self,model_name,color,mileage):
        self.name=model_name
        self.cl=color
        self.m=mileage
a=royalenfield("xyz","red",10)
b=royalenfield("ful","nule",30)
c=royalenfield("husjs","black",40)
print(a.name,a.cl,a.m)
print(b.name,b.cl,b.m)
print(c.name,c.cl,c.m)
