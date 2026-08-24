t1 = (25)
t2 = (25,)
t3 = 25,
print(type(t1), type(t2), type(t3))     # ①
t4 = ('東', '南', '西')
a, b, c = t4
print(b)                                 # ②
t5 = t4 + ('北',)
print(t5, len(t5))                       # ③

print(sum((10, 20, 30), 40))             # ④

lst = list(t5)
lst.append('東北')
print(tuple(lst))                        # ⑤
#t4[0] = '中'                              # ⑥ 這行會發生什麼事？