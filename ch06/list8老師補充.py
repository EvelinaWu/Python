lst1 = [10,20,30,40,50]

#num=len(lst1)
#print(str(num))  原本是這樣寫的
print(str(num := len(lst1) ))

#也可以用f-string
print(f'total={sum(lst1)}')

#要取最大值 
#先傳統的方法
big = max(lst1)
print(str(big)) #透過兩行可以將最大值輸出

#底下為f-string
print(f'min={min(lst1)}')