from snack import Snack
class Inventory:
    
     def __init__(self):
          self.records={}
          self.sales_records=[]
          ob1= Snack(1,"Smosa",10,20,True)
          self.records[ob1.id]=ob1
          ob2= Snack(2,"Biscuit",20,40,True)
          self.records[ob2.id]= ob2
          ob3= Snack(3,"Tea",10,10,True)
          self.records[ob3.id]=ob3
          ob4= Snack(4,"Noodles",30,20,True)
          self.records[ob4.id]=ob4

    
     def addSnack(self,snackob):
          if snackob.id in self.records:
              ob= self.records[snackob.id]
              ob.quantity=ob.quantity+snackob.quantity
              ob.availability=True
              self.records.update({ob.id:ob})
          else:
               self.records[snackob.id]=snackob

          return;

     def removeSnack(self,snakeId):
          if snakeId in self.records:
               ob= self.records[snakeId]
               ob.quantity= ob.quantity-1
               if ob.quantity<=0:
                    ob.availability=False
               self.records.update({ob.id:ob})
               return True;
          else:
               print("Invalid snack id ");
               return False;
          

     def updateAvailability(self,snakeId):
          if snakeId in self.records:
               ob=self.records[snakeId]
               if ob.availability==True:
                    ob.availability=False
               else:
                    ob.availability=True
               return True;
          else:
                print("Invalid snack id ");
                return False;      

     def updateSalesRecords(self,itemId):
          if itemId in self.records:
               ob= self.records[itemId]
               if ob.availability==True:
                    self.removeSnack(itemId)
               else:
                    print("#####################################")
                    print("Item is not avaliable for sale")
                    return

          self.sales_records.append(itemId)
          print("#####################################")
          print("Records has been updated sucessfully")
          return;

     def viewSalesRecords(self):
          tmp={}
          for i in self.sales_records:
               if i in tmp:
                    sale= tmp[i]
                    sale +=1;
                    tmp.update({i:sale})
               else:
                    tmp[i]=1

          print("Item id : No of sold quantity")
          for id,sale_quantity in tmp.items():
               print(f" {id} : {sale_quantity}")
          return;

     def viewAllSnacks(self):
          for id,snack in self.records.items():
               if(snack.availability==True):
                    print(snack)

          return;
            

          
               
     