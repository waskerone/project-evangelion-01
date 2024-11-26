arr = list()
n = int(input("Введите колличество эллементов массива:"))
i = 0
while (i < n):
    tmp = int(input(""))
    arr.append(tmp)
    i += 1
print("Массив:")
i = 0
while (i < n):
    print(arr[i], end=" ")
    i += 1
print("")