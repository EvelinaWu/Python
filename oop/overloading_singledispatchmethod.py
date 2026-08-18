from functools import singledispatchmethod
class calculator():
  @singledispatchmethod #通常這是用第一個參數做判斷 假設第一個參數式int型態則會用第一種方法
  def add(self, x, y= None):
     if y is not None:
        return f"數字相加結果：{x + y}"
      
   #假設是str型態則會用第二段 要註冊一個方法 就是add.register
  @add.register
  def _(self, x: str, y: str):
        return f"字串串接結果：{x} - {y}"
    
    #甚麼表示方法(都沒有註冊的話 就會用第一段方法)
   # ______________________測試執行_______________________
calc= calculator( )
print(calc.add(5))
print(calc.add(10,20))  
print(calc.add("Hello","World"))