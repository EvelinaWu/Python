set1 = {'Anastasia'}
print(set1)

set1 = set('Anastasia')#會被拆成一個一個的字母，並去判斷是否有重複的字母
print(set1)


set1 = set({'貓':'cat','狗':'dog'})#會被拆成一個一個的字母，並去判斷是否有重複的字母
print(set1)


set1 = set('嘻嘻哈哈')#會被拆成一個一個的字母，並去判斷是否有重複的字母
print(set1)

set1.add('笑嘻嘻')
print(set1)

set1.remove('笑嘻嘻')
print(set1)

set1.discard('笑嘻嘻')  #刪除set裡的元素，如果沒有這個元素也不會報錯

set1.update('笑嘻嘻')  #將set1裡的元素更新成笑嘻嘻這個字串裡的每一個字母
print(set1) 

#set1.remove('笑嘻嘻')  #刪除set裡的元素，如果沒有這個元素會報錯
set1.pop()

print(set1)  #隨機刪掉一個元素，並回傳該元素