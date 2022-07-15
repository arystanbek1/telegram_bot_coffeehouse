# count = ''
# for i in range(20):
#     count += str(1)
#     print(count + '\n', end= '')


def func():
    arr1 = []
    arr2 = []
    for i in range(0, 4):
        arr1.append(i)
    for i in arr1:
        if i % 2 != 0:
            arr2.append(i)
    sum = 0
    a = 0
    arr3 = []
    for i in arr1:
        a = i ** 2
        for j in arr2:
            if j < a:
                sum += i
    return sum





print(func())


