class main(object):
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def disp(self):
        print(f'Employee ID : {self.id}')
        print(f'Employeed Name: {self.name}')
class sub(main):
    def __init__(self, name, id,age,sal):
        self.age=age
        self.sal=sal
        main.__init__(self,name,id)
    def info(self):
        print("Employee Salary: ",self.sal)
        print("Employee Age : ",self.age)
        
        
a=sub("Rishik",103,29,50000)
a.disp()
a.info()
