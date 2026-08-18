dict1 = dict((('一月','正月'),('二月','花月'),('三月','桃月')))
#dict = dict(('一月','正月'),('二月','花月'),('三月','桃月'))
#會有問題 因為在字典裡只接受一個引數/參數

print(dict1)


dict2 = dict.fromkeys(('四月','五月'))
print(dict2)  #會傳回一個新的字典，裡面有兩個鍵值對，值都是None

dict2 = dict.fromkeys(['一月','四月'],'端月')
print(dict2)

print('dict1=',dict1)
#dict1.update(dict2)  #將dict2裡的鍵值對更新到 dict1裡面
#print('dict1=',dict1)
print(dict1.keys())

#也可以去找所有的value
print(dict1.values())
print(tuple(dict1.values()))  #若希望得到tuple的資料型態，將dict1裡的所有value轉換成tuple 
#可以看到取得的是dict_values(['正月', '花月', '桃月'])

print(dict1.items())  #會傳回一個dict_items的物件，裡面有三個元素，每個元素都是一個tuple
#可以先透過item的方法抓出來 
#一對一對的cube內容再傳回list裡面
print(list(dict1.items()))#為甚麼要再轉一次 一樣的內容 已經是list就可以不再用list了 老師已修正


print('dict2=',dict2)
print(dict2.get('三月'))  #會傳回None，因為dict2裡沒有三月這個key

dict2.setdefault('一月','梅月') #(key,預設值) #會傳回'端月'，因為dict2裡有一月這個key，且值是'端月'
print(dict2)

dict2.setdefault('五月','梅月') 
print(dict2)

dict2.setdefault('四月','梅月') 
print(dict2)

dict2.setdefault('七月','梅月') 
print(dict2)
dict2.setdefault('二月','梅月') 
print(dict2)

#使用此功能之目的　先回傳再刪掉
print(dict2.pop('二月'))  #先回傳再刪掉二月這個鍵值對
print(dict2)

print(dict2.popitem())  #會隨機刪掉一個鍵值對，並回傳該鍵值對
print(dict2)

dict3 ={}
#print(dict3.popitem())


# ============= update =============
# 使用 update() 整合兩個字典：將 dict2 中的所有鍵值對合併至 dict1 中
# 若 Key 已存在（如 '一月'），dict2 的值 ('端月') 會覆蓋 dict1 原本的值 ('正月')
# dict1={'一月': '正月'}
# dict2={'一月': '端月', '四月': '端月'}
dict1.update(dict2)
print(dict1)
# 輸出結果 {'一月': '端月', '四月': '端月'} 

dict1.clear()
print(dict1)