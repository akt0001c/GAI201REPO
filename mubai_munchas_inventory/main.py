from inventory import Inventory
from snack import Snack

print("Welcome in Mumbai Muncheis")
print("*****************************")
print("\n")

myInventory= Inventory()
option=0
while(True):
    print("Press Button according to your choice:")
    print("**************************************")
    print("\n")
    print("=========================================================")
    print("|| Press 1 for Adding Snack into inventory             ||")
    print("|| Press 2 for Removing Scack from inventory           ||")
    print("|| Press 3 for Updating the availalibility of the item ||")
    print("|| Press 4 for selling of an item                      ||")
    print("|| Press 5 for View all  avaliable snacks              ||")
    print("|| Press 6 for Exit                                    ||")
    print("=========================================================")
    print("\n")

    string_op= input("Enter a choice :")
    option= int(string_op)

    if(option==1):
        id= int(input("Enter Snack id: "))
        name= input("Enter Snack name: ")
        price=int(input("Enter Snack price: "))
        quantity=int(input("Enter Snack quantity: "))
        snacksOb= Snack(id,name,price,quantity,True)
        
        myInventory.addSnack(snacksOb)

        print("#####################################")
        print("Snacks added sucessfully")
    elif(option==2):
        id= int(input("Enter Snack id: "))

        checker= myInventory.removeSnack(id)
        if(checker==True):
            print("#####################################")
            print("Snack removed sucessfully")
    elif(option==3):
       id= int(input("Enter Snack id: "))
       checker= myInventory.updateAvailability(id)
       if(checker==True):
            print("#####################################")
            print("Snack status updated sucessfully")
    elif(option==4):
        id= int(input("Enter Snack id: "))
        myInventory.updateSalesRecords()
        myInventory.updateSalesRecords()
    elif(option==5):
        myInventory.viewAllSnacks()
    elif(option==6):
         print("#####################################")
         print("Thank you for using our service ,Exit")
         print("\n")
         break;
    else:
        print("#################################")
        print("Invalid Choice ,Please try again")

    if option ==6:
        print("#####################################")
        print("Thank you for using our service ,Exit")
        print("\n")
        break;
