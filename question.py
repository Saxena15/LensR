

s = str(input())


i = 0
if s[i] == 'a':
    if s[i+1] == 'a':
        i += 1

    elif s[i+1] == 'b':
        i += 1
        if s[i+1] != 'b':
            print('No')
            i += 1

        else:
            print('Yes')
            i += 1
    else:
        print('No')

    i += 1
else:
    print('No')
