class shape(object):
    def __init__(self):
         print("I am a polygon")
        
   
class square(shape):
    def __init__(self):
        super().__init__()
        print("I have 4 sides")
        
class triangle(shape):
    def __init__(self):
        super().__init__()
        print("I have 3 sides")
class pentagon(shape):
    def __init__(self):
        super().__init__()
        print("I have 5 sides")
s=square()
t=triangle()
p=pentagon()