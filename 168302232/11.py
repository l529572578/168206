def find_thief():
    thief = 'A'
    flag = 0
    a = (thief != 'A')
    b = (thief == 'D')
    c = (thief == 'B')
    d = (thief != 'D')
    for i in range(4):
        thief = chr(ord(thief) + i)
        add = a + b + c + d
        if add == 1:
            flag = 1
            if a:
                print('A说的是真话')
            if b:
                print('B说的是真话')
            if c:
                print('C说的是真话')
            if d:
                print('D说的是真话')
            print(thief + '是偷钻石的罪犯')
            break
    if flag == 0:
        print('无法找到罪犯')


find_thief()
