class main(object):
    def __init__(self,ln,fn):
        self.last=ln
        self.first=fn
    def name(self):
        print(f'Student First Name : {self.first}')
        print(f'Student Last Name : {self.last}')
        print("Student Full Name :",self.first+" "+ self.last)
class Student(main):
    def __init__(self, ln, fn,age):
        super().__init__(ln, fn)
        self.age=age
    def a(self):
        print(f'Student Age : {self.age}')

a=Student("Goyal","Rishik",14)
a.a()
a.name()
    

