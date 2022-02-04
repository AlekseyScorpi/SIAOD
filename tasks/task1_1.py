def func():
    data = input().strip().replace("  ", " ").split(" ")
    arr = [int(el) for el in data]
    p = 0
    if len(arr) < 3:
        return p
    arr.sort()
    j = len(arr) - 1
    print(arr)
    while j > 1:
        a = arr[j]
        b = arr[j - 1]
        c = arr[j - 2]
        if (b + c) > a:
            p = a + b + c
            return p
        j -= 1
    return p


print(func())
