import os
os.system('cls' if os.name == 'nt' else 'clear')
import random

item_list=["rock","paper","scissors"]
print("__________________")
print("|     1.rock      |")
print("|     2.paper     | ")
print("|     3.scissors  |")
print("-------------------")
user_choice=(input("enter your choice  :   "))
if user_choice !="rock" and user_choice!="paper" and user_choice!="scissors":
   print("invalid choice")

else:
 comp_choice=random.choice(item_list)

 print(f"your choice is {user_choice} and computers choice is {comp_choice}")

 if user_choice==comp_choice:
    print("both choose the same: Match is Tied")
 elif user_choice=="rock":
    if comp_choice=="paper":
     print("you lose")
    else:
      print("===========")
      print ("You win")
      print("===========")
 elif user_choice=="paper":
    if comp_choice=="scissors":
     print("===========")    
     print("you lose")
     print("===========")
    else:
       print("===========")
       print("you win")
       print("===========")
 elif user_choice:="scissors":
    if comp_choice =="rock":
      print("===========")
      print("you lose")
      print("===========")
    else:
       print("===========")
       print("you win")
       print("===========")
                