# Codewars - 8 kyu
#build basic class for Human, subclasses for Man and Woman
#god func creates one object of each class man and woman and 
#returns an array with the objects

def God():
    adam = Man("Adam")
    eve = Woman("Eve")
    
    return [adam, eve]

class Human():
    def __init__(self, name):
        self.name = name
        
class Man(Human):
    def __init__(self, name):
        super().__init__(name)
    
class Woman(Human):
    def __init__(self, name):
        super().__init__(name)