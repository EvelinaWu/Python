lst = [10, 20, 30, 40, 50]
lst.append(60)
lst.insert(2, 25)
print(lst)                      # ①

lst.remove(30)
x = lst.pop()
print(lst, x)                   # ②

print(lst.index(40), lst.count(20))   # ③

del lst[1:3]
print(lst)                      # ④

print(lst + [7, 8], lst * 2)    # ⑤