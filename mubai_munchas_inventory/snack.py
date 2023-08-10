class Snack:
    

    def __init__(self,id,name,price,quantity,availability):
        self.id=id
        self.name=name
        self.price=price
        self.quantity=quantity
        self.availability=availability


    def __str__(self):
        return f"Snack id: {self.id}, Snack name: {self.name} , Snack price: {self.price} ,Snack availability: {self.availability}"

        