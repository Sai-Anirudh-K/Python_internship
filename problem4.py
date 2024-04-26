'''take string from user and print all vowels of the string


s=input()
p="AEIOUaeiou"
for i in s:
    for j in p:
        if(i==j):
            print(i)'''

s=input()
for i in s:
    if i in 'aeiouAEIOU':
        print(i,end=" ")