from Dishes import Dishes

class DishMenu:
    dishMenu={
      1:Dishes(1,"Palak Panner",100,"Yes"),
      2:Dishes(2,"dal-Rice",200,"Yes"),
      3:Dishes(3,"Roti",10,"Yes"),
      4:Dishes(4,"shahi panner",150,"Yes"),
      5:Dishes(5,"Malai kophta",50,"Yes") 
       }
    
    def __init__(self):
        return
    
    @staticmethod
    def displayMenu():
        for dishid,dish in DishMenu.dishMenu.items():
            if dish.available=="Yes" or dish.available=="yes":
                print("################################################################")
                print("\n")
                print(f"#id : {dishid} ,DishName : {dish.name}, Price : {dish.price} ")
                print("\n")

        print("################################################################")