class Animal:
  #先建立一個建構式
  def __init__(self, name, age):
    self.age = age
  def sing(self): #定義方法
    print(self.name + str(self.age) + "， 很會唱歌!")
    
  def grow(self,year):
    self.age = self.age + year  
    
  Animal("鸚鵡",1).grow(1)
  Animal("鸚鵡",1).sing()
  