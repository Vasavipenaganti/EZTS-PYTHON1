'''class college:
    def __init__(self,name):
          self.name=name    
          self.ece1()
          self.ece2()
    def ece1(self):
          print("This is ece1",self.name)
    def ece2(self):
          print("This is ece2",self.name)
s = input()
obj=college(s)'''

'''
>>>pragati
This is ece1 pragati
This is ece2 pragati'''

#using return
class college:
    def __init__(self):
        print(self.sec1())
        print(self.sec2())
    def sec1(self):
          return "method 1"
    def sec2(self):
          return "method 2"
obj=college()

'''method 1
method 2'''
        

