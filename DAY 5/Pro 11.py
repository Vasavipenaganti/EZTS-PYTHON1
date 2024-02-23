#oops en
'''class student:
    def __init__(self,name,age,sec):               #init-constructor- a method intilaise itself when to create a obj
          self.name=name                                #self calls the name variable
          self.age=age
          self.sec=sec
          print(name,age,sec)
obj=student("Vasavi","22","ece-2")
obj1=student("Poorna","90","ece-1")'''

'''Vasavi 22 ece-2
Poorna 90 ece-1'''

class ece:
    def section1(self,name,rollno):
          self.name=name
          self.rollno=rollno
          print(name,rollno)
    def section2(self,n,rno,age):
          self.n=n
          self.rno=rno
          self.age=age
          print(n,rno,age)
obj = ece()
obj.section1("Vasavi","485")
obj.section2("poor",490,53)

'''Vasavi 485
poor 490 53'''

    

