class Animal:
  def __init__(self, name, age):
    self.name = name #定義私用屬性
    self.age = age #定義私用屬性
  def sing(self): #定義私用方法
    print(self._name + str(self._age) + "， 很會唱歌!")
    
  def talk(self): #定義共用方法
    print("也會模仿人類說話!")
    
bird=Animal("灰鸚鵡",2)
bird.talk()
bird.__age = -1
bird.talk()
#bird.__sing() #會報錯，因為sing()是私用方法 執行錯誤