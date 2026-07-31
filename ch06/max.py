lst =[ 0 for x in range(5)]
print('請按照順序輸入五個整數:')
for i in range(5):
  print( f'輸入第{i+1}個元素內容:', end= '')
  lst[i]=eval(input())

  max = lst[0]
  for item in lst:
    if item >max:
      max = item
print()
print(f'最大值為{max}')