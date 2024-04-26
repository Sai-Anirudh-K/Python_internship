'''take integer from user and reverse the number
n=int(input())
def rev(n):
    res=0
    while n>0:
        res=res*10+n%10
        n=n//10
    return res
print(rev(n))'''

n=input()
print(n[::-1])        #palindrome if n==n[::-1]: print("palindrome")