class Animal:
   def __init__(self,name,age):
        self.name = name #定義屬性
        self.age = age
   def sing(self): #定義方法
        print(self.name+"， 很會唱歌!")
        
   def grow(self,year):
        self.age = self.age + year
        
bird = Animal("鸚鵡",1)
print(bird.name)
bird.grow(1)
bird.sing()