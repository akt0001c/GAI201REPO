from MenuOperations import MenuOperations
from DishMenu import DishMenu


print("*******************************")
print("*Welcome in Zomoto Chronicles *")
print("*******************************")

option=0
MenuOperations.loadData("data.txt")

while(True):
    print("This is our menu ,Please select any one option")
    print("\n")
    DishMenu.displayMenu()
    print("\n")

    print("***********************************************")
    print("* Press 1 for adding a dishe into the menu    *")
    print("* Press 2 for Removing a dish from the menu   *")
    print("* Press 3 for Placing an order                *")
    print("* Press 4 for displaying order list           *")
    print("* Press 5 for updating an order status        *")
    print("***********************************************")
    print("\n")

    

    print("======================================================")
    option= int(input("Please Enter your choice or enter -1 to exit : "))
    print("======================================================")

    if(option== -1):
        MenuOperations.saveData("data.txt")
        print("Thank you for using our services , exit")
        break

    if(option==1):
        MenuOperations.addDishes()
    elif(option==2):
        dishid=input("Enter Dish id :")
        MenuOperations.removeDish(dishid)
    elif(option==3):
        MenuOperations.takeOrder()
    elif(option==4):
       checker= input("Do you want to see orders with a particular status  then enter y or enter n:")
       if checker=='y':
        status= input("Enter the order status : ")
        MenuOperations.displayOrders(status)
       else:
        MenuOperations.displayOrders()
    elif(option==5):
        MenuOperations.updateOrderStatus()
    else:
        print("Invalid Choice ,Please try again")

    

