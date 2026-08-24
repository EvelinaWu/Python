a = [5, -3, 8, 1, -7]

for loop in range(1, 5):
    for index in range(0, 5 - loop):
        if a[index] > a[index + 1]:
            a[index], a[index + 1] = a[index + 1], a[index]  # 請寫出交換兩元素的敘述
    print(f'第 {loop} 次排列:', a)