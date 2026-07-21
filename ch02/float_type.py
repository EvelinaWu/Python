f,i =1.2345, 12345#我設兩個變數
print(type(f))
f2=float(i)
print(f2)
print(float.is_integer(f))
#來檢查一個浮點數數值是否等於整數(及小數點後是否全為0)
print(float.is_integer(f2))
#資料型態是否為整數
print(isinstance(f2,int))
print(round(f,2))
print(round(f))
