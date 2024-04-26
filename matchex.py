a=8
match a:
    case 1:
        print('1')
    case 2:
        print('2')
    case 8:
        print('8')
    case _:                             #default case
        print('default')