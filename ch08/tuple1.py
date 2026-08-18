tuple1 = ('東','南','西')
print(tuple1) 
east, south, west = tuple1 #解構
print(east)
print(south)
print(west)
#再新增一個北將他asign給tuple1
#在宣告一個元素時是這樣寫
tuple2 = tuple1 + ('北',)
print(tuple2)
print(tuple1)
tuple1,tuple2 = tuple2,tuple1
print(tuple2) 
print(tuple1)
print(len(tuple2))  #計算tuple2的長度


#del (tuple2)  #刪除tuple2 
print(tuple2)  #會出現錯誤，因為tuple2已經被刪除

#宣告一個元素 list裡可以是元素
list1 = list(tuple1)
print(list1)

list1.append('東北')  #在list1裡新增一個元素
print(list1)

tuple1 = tuple(list1)  #將list1轉換成tuple1
print(tuple1)

print('東北' in tuple1)  #判斷tuple1裡是否有'東北'

for t in tuple1:  #使用for迴圈將tuple1裡的元素一個一個印出來
    print(t, end=',')