from Dishes import Dishes
from Orders import Orders
from DishMenu import DishMenu
import os
import pickle


    

class MenuOperations:
    orders_list=[]

    @staticmethod
    def addDishes():
        dishid= int(input("Enter new dish id :"))
        name= input("Enter dish name :")
        price= int(input("Enter dish price :"))
        ob= Dishes(dishid,name,price,"Yes")
        DishMenu.dishMenu[ob.id]=ob;
        print("Dish added sucessfully")
        return
    
    @staticmethod
    def removeDish(dishid):
        dishid= int(dishid)
        if dishid in DishMenu.dishMenu:
            del DishMenu.dishMenu[dishid]
            print("Dish removed successfully")
        else:
            print("Dish is not present in the menu")
            


    @staticmethod
    def takeOrder():
        customer_name=input("Enter customer name :")
        dishList= [ int(id) for id in  input("Enter dishes id which are seperated with commas :").split(',')]
        OrderOb= Orders.takeOrder(customer_name,dishList)
        MenuOperations.orders_list.append(OrderOb)
        print("Order placed Sucessfully")
        return ;

    @staticmethod
    def updateOrderStatus():
        order_id= int(input("Enter order id : "))
        order_status= input("Enter New Order Status :")

        for orderobj in MenuOperations.orders_list:
            if(orderobj.id== order_id):
                orderobj.changeStatus(order_status)
                print("Order status changed sucessfully")
                return;

        print("Order id not found")
        return;

    @staticmethod
    def displayOrders(status=None):
        for order in MenuOperations.orders_list:
            if status is None or order.status== status:
                print(order)
                total_Bill= order.calculatePrice()
                print(f"Tota Bill amount for this order : {total_Bill}")
            else:
                print("Orders not Found for particular status")
        
    @staticmethod
    def saveData(fileName):
        data= (DishMenu.dishMenu,MenuOperations.orders_list)
        with open(fileName,"wb") as file:
            pickle.dump(data,file)
        print("Data saved sucessfully")
        return;


    @staticmethod
    def loadData(fileName):
        try:
            if(os.path.exists(fileName)  and os.path.getsize(fileName)>0):
                with open(fileName,"rb") as file:
                  data= pickle.load(file)
                  DishMenu.dishMenu,MenuOperations.orders_list=data
                  print("Data loaded sucessfully")
            else:
                print("File not found or empty")
     
        except FileNotFoundError:
            print("Data file not found")
    




        

