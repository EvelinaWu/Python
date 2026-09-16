class Animal:
    def __init__(self, name): #初始化方法，建構方法/建構子/constructor
        self.name = name

    def fly(self):
        print(f"{self.name} is flying.")
class Bird(animal):#繼承自Animal類別
    def __init__(self, name, species):
        super().__init__(name) #呼叫父類別的初始化方法
        self.species = species

    def fly(self):
        print(f"{self.name} the {self.species} is flying high!")