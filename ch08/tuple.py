#傳回元組內所有元素的總和
t1 = (10,20,30)
print(sum(t1,40))
#先將10+20+30=60，再加上40，總和為100

list1 = [10,20,30]
print(sum(list1,40))
print(tuple(list1))


tuple1 = (10,20,30)
print(list(tuple1))

print(t1.count(20))  #計算20在t1中出現的次數

t1 = (50,20,40,30,60,70,10)
print(sorted(t1))  #將t1排序，並傳回一個新的list