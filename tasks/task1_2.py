def func():
    data = input().strip().replace("  ", " ").split(" ")
    data.sort(reverse=True)
    result = ""
    i = 0
    temp = []
    while i < len(data):
        temp.append(data[i])
        symbol = data[i][0]
        if i + 1 >= len(data):
            result += "".join(temp)
            break
        if symbol != data[i + 1][0]:
            temp.sort(reverse=True)
            tempValue = temp[-1]
            temp.pop(-1)
            temp.insert(0, tempValue)
            result += "".join(temp)
            temp = []
        i += 1
    return result


print(func())