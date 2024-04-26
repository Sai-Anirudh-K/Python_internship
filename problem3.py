'''check whether a character is a vowel or not'''

f=input()
'''match f:
    case 'a':
        print('vowel')
    case 'e':
        print('vowel')
    case 'i':
        print('vowel')
    case 'o':
        print('vowel')
    case 'u':
        print('vowel')
    case _:
        print("not vowel")'''

s='aeiouAEIOU'
if f in s:                   #or f in 'aeiouAEIOU
    print("vowel")
else:
    print("not a vowel")