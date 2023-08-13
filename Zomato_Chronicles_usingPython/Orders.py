from Dishes import Dishes
from MenuOperations import MenuOperations

class Orders:
    orderId=100;
    def __init__(self,customer_name,id ):
        self.id=id
        self.customer_name=customer_name;
        self.Ordered_dishes=[]
        self.status="Received"


    def __str__(self):
          return f" Order id : {self.id} , Ordered by : {self.customer_name}, Ordered dishes : {self.Ordered_dishes} ,Order Status : {self.status},"
    

    def addDish(self,dish):
         self.Ordered_dishes.append(dish)

    def changeStatus(self,newStatus):
        self.status=newStatus;
    
    def calculatePrice(self):
        total_price=0
        for dish in self.Ordered_dishes:
            total_price= total_price + dish.price

        return total_price;

    @staticmethod
    def takeOrder(name,dish_id_list):
        order= Orders(name ,Orders.orderId)
        Orders.orderId= Orders.orderId+1
        
        
        for dishId in dish_id_list:
            if dishId in MenuOperations.DishMenu:
                dish= MenuOperations.DishMenu[dishId]
                if(dish.available==True):
                    order.addDish(dish)
                else:
                    print(f" {dish.name}  is not available")
            else:
                print(f"Dish with id {dishId}  is not present in menu")

        return order;
    

