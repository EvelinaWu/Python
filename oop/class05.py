class Animal(): #先建立一個
    def __init__(self, name): #初始化的時候要把名字先做一個設定
      #在初始化的時候還要建立一個方法
      self.name = name #定義屬性
      
    def fly(self): #宣告一個fly 誰很會飛
        print(self.name + " 很會飛!")
        
        #上述沒有就是公開的方法，
class Bird(Animal): #因為繼承父類別的時候，子類別可以使用父類別的屬性和方法
    def __init__(self, name):
        self.name ="粉紅色"+name  #子類別可以覆寫父類別的屬性
    def sing(self): #子類別可以覆寫父類別的方法
        print(self.name + " 也愛唱歌!")

piegon = Animal("小白鴿") #建立一個Animal的類別，建立一個小白鴿的物件
piegon.fly()

parrot = Bird("鸚鵡") #建立一個Bird的類別，建立一個鸚鵡的物件
parrot.fly() #呼叫父類別的方法 粉紅色小鸚鵡很會飛
parrot.sing() #呼叫子類別的方法 粉紅色小鸚鵡也愛唱歌

#如何使用class的繼承，子類別可以使用父類別的屬性和方法，子類別也可以覆寫父類別的屬性和方法