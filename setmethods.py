a={1,5,7,8,3}
a.add(9)
a.pop()    #deletes randomly
a.remove(9)   #if element not present it will show error
a.discard(2)   #it will not show error
b={4,7,8}
a.union(b)      #it returns total a and b and does not make changes
a.update(b)  #make changes
a|b       #union using operator
a.intersection(b)
a.intersection_update(b)
a&b #intersection using operator
a.difference(b)  #removes common elements
a.difference_update(b)   #symmetric difference means uncommon elements of both the sets
a-b #difference using operators
a.symmetric_difference(b)
a.symmetric_difference_update(b)
a^b  #symmetric difference using operators
a>=b  #to find a is superset of b
a>b  #proper superset
a.issuperset(b)
a.issubset(b)
a<=b  #subset
a<b #proper subset
a.isdisjoint(b) #if no intersection returns True

