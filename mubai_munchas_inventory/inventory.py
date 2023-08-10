from snack import Snack
class Inventory:
    
     def __init__(self):
          self.records={}
          ob1= Snack(1,"Smosa",10,20,True)
          self.records[ob1.id]=ob1
          ob2= Snack(2,"Biscuit",20,40,True)
          self.records[ob2.id]= ob2
          ob3= Snack(3,"Tea",10,10,True)
          self.records[ob3.id]=ob3
          ob4= Snack(4,"Noodles",30,20,True)
          self.records[ob4.id]=ob4

    
     def addSnake(self,snakeob):
          if snakeob.id in self.records:
               
               
     