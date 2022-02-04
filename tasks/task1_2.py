def func():
    data = input().strip().replace("  ", " ").split(" ")
    data.sort(reverse=True)
    print(data)
    arr = []
    i = 0
    while i < len(data):
        symbol = data[i][0]

    result = ""
    for i in arr:
        result += i
    return result


print(func())