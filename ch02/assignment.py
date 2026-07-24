x=5#指定x變數值為常值5
y=x#指定y變數值為變數X的值
print(id(x),id(y))#顯示變數x,y的記憶體位置
x=3+y #指定X變數值為運算式3+y的結果
print(id(x))
a,b=2,3
print(id(a),id(b))
a,b=b,a #a,b變數值交換
print(id(a),id(b))