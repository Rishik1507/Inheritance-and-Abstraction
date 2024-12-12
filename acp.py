class shape(object):
    def __init__(self):
         print("I am a polygon")
        
   
class square(shape):

    def __init__(self,side):
        super().__init__()
        print("I have 4 sides")
        self.side=side
        print(f'Area is: {self.side*self.side}')
    
class triangle(shape):
    def __init__(self,base,height):
        super().__init__()
        print("I have 3 sides")
        self.base=base
        self.height=height
        print(f'Area is : {1/2*self.base*self.height}')

s=square(4)
t=triangle(3,5)
