from Dishes import Dishes
from Orders import Orders
import pickle


class MenuOperations:
    orders_list=[]
    DishMenu={
      1:Dishes(1,"Palak Panner",100,"Yes"),
      2:Dishes(2,"dal-Rice",200,"Yes"),
      3:Dishes(3,"Roti",10,"Yes"),
      4:Dishes(4,"shahi panner",150,"Yes"),
      5:Dishes(5,"Malai kophta",50,"Yes") 
       }
    
    @staticmethod
    def addDishes():
        id= int(input("Enter new dish id :"))
        name= input("Enter dish name :")
        price= int(input("Enter dish price :"))
        ob= Dishes(id,name,price,"Yes")
        MenuOperations.DishMenu[ob.id]=ob;
        print("Dish added sucessfully")
        return

    @staticmethod
    def takeOrder():
        customer_name=input("Enter customer name :")
        dishList= [ int(id) for id in  input("Enter dishes id which are seperated with commas :").split(',')]
        OrderOb= Orders.takeOrder(customer_name,dishList)
        MenuOperations.orders_list.append(OrderOb)
        return;

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
        
    @staticmethod
    def saveData(fileName):
        data= (MenuOperations.DishMenu,MenuOperations.orders_list)
        with open(fileName,"wb") as file:
            pickle.dump(data,file)
        print("Data saved sucessfully")
        return;


    @staticmethod
    def loadData(fileName):
        try:
            with open(fileName,"rb") as file:
                  data= pickle.loads(file)
                  MenuOperations.DishMenu,MenuOperations.orders_list=data
                  print("Data loaded sucessfully")
     
        except FileNotFoundError:
            print("Data file not found")
    




        

