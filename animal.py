from abc import ABC

class animal(ABC):
    def move(self):
        pass

class human(animal):
    def move(self):
        print("I can Walk")
class fish(animal):
    def move(self):
        print("I can Swim")
class cat(animal):
    def move(self):
        print("I can meow")
class dog(animal):
    def move(self):
        print("I can Bark")
h=human()
h.move()
d=dog()
d.move()
c=cat()
c.move()
f=fish()
f.move()