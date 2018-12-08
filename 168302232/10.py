#死算
start = 'hit'
end = 'cog'


def find_path(start, end):
    first = list(start)
    final = list(end)
    if start == end:
        return "start = end"
    else:
        for i in range(len(start)):
            for j in range(ord('a'), ord('z')+1):
                if first[i] == final[i]:
                    break
                else:
                    print(''.join(first))
                    first[i] = chr(j)
        print(''.join(first))


find_path(start, end)


#使用二分法
start = 'hit'
end = 'cog'


def find_path(start, end):
    first = list(start)
    final = list(end)
    low = ord('a')
    high = ord('z')
    if start == end:
        return "start = end"
    else:
        for i in range(len(start)):
            s = ''.join(first)
            e = ''.join(final)
            while(s != e):
                if first[i] == final[i]:
                    break
                else:
                    item = ord(final[i])
                    first = binary(i, first, low, high, item)
                    s = ''.join(first)
    print(s)

def binary(i, first, low, high, item):
    if low > high:
        return
    print(''.join(first))
    mid = int((low + high) / 2)
    first[i] = chr(mid)
    if item < mid:
        return binary(i, first, low, mid, item)
    if item > mid:
        return binary(i, first, mid, high, item)
    return first


find_path(start, end)
