data = (('香蕉',34,2),('芭樂',28,3),('水梨',50,2))
total = []
print('品 名\t數 量\t單 價\t小 計')

for t1 in data:
  #要將上述元組的元素解構成三個變數
  #name, price, quantity = t1
  #subtotal = price * quantity
  #print(f'{name}\t{quantity}\t{price}\t{subtotal}')
  
  #解構出來的，是他們的品名、數量、單價
  name,s1,s2 = t1
  print(f'{name:>4}{s1:>4}{s2:8}{total[-1]:8}')
  
  print(f'總 計:{sum(total):23}')
  
 