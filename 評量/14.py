def f(n, lst):
    n = n * 2
    lst.append(99)
    v = 10
    global g
    g = g + 1
    print('函式內 :', n, lst, v, g)

g = 100
n = 5
data = [1, 2]
v = 0

f(n, data)
print('函式外 :', n, data, v, g)