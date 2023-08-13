class Dishes:
    def __init__(self,id,name,price,available):
        self.id=id
        self.name=name
        self.price=price
        self.available=available
        

    def __str__(self):
        return f"Dish id : {self.id} ,Dish Name : {self.name} , Dish Price : {self.price} , Available :{self.available}"
        
        