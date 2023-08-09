import random

user_rounds=0
comp_rounds=0
draws=0
round=1
list1= ["rock","paper","scissors"];


def startGame():
    global round,user_rounds,comp_rounds,draws

    print(f"Round {round} started")
    print("-----------------")
    print("If you want to quit the game Press y or else press n for continue")
    checker= input("Press y or n : ")
    if checker=="y":
        return
    else:
        print("Now you can play the game")

    print("***********************************")

    print("You have to choose one from among these choices : ")
    print("------------------")
    print("Press 1 for Rock")
    print("press 2 for Paper")
    print("press 3 for Scissor")
    string_choice= input("Enter a choice:")
    choice= int(string_choice)
    user_choice=list1[choice-1]
    print("********************************")
    print(f"User has selected {user_choice}")
    print("********************************")
    print("\n")
    comp_choice= random.choice(list1)
    print("********************************")
    print(f"Computer has selected {comp_choice}")
    print("********************************")
    print("\n")


    if(user_choice==comp_choice):
        print("********************************")
        print(f"Round{round} Match Draw")
        print("********************************")
        draws +=1
        round +=1
        startGame()
    elif((user_choice==list1[0] and comp_choice==list1[2]) or (user_choice==list1[1] and comp_choice==list1[0]) ):
        print("********************************")
        print("User has won this round")
        print("********************************")
        round +=1
        user_rounds +=1
        startGame()
    else:
        print("********************************")
        print("Computer has won this round")
        print("********************************")
        round +=1
        comp_rounds +=1
        startGame()
   
    return


print("Welcome in Rock,Paper,Scissor")
print("==================================")
print("If you want to start the game press 1 else press 0")
num= input("Enter a choice:")
if int(num)==1:
    startGame()
else:
    print("Thank you for visit,you can play later")


print(f"Total Round played: {round}")
print(f"User won : {user_rounds} rounds")
print(f"Computer won: {comp_rounds} rounds")
print(f"Total draw :{draws}")

