# Lauren Cook
# feb 10 2022
# rock paper scissors game

from random import randint
import random 
from time import sleep

def decide_winner():
    uscore = 0
    cscore = 0
    
    while uscore < 3 and cscore < 3:
        user_choice = input("Choose between R, P, or S").upper()
        options = ["R", "P", "S"]
        computer_choice = options[randint(0,2)]
        
        print("Computer selecting. . .")
        sleep(2)
        print("Computer choice" + computer_choice)
        sleep(1)
        if user_choice == computer_choice:
            print("It's a tie! CAT!")
        elif user_choice == "P" and computer_choice == "R":
            print("You win, overthrowing technology for now!")
            uscore = uscore + 1
        elif user_choice == "S" and computer_choice == "P":
            print("You win, overthrowing technology for now!")
            uscore = uscore + 1
        elif user_choice == "R" and computer_choice == "S":
            print("You win, overthrowing technology for now!")
            uscore = uscore + 1
        else:
            print("You lost to a computer, you buffon, you clown, you silly goose.")
            cscore = cscore + 1
        print("User score: " + str(uscore) + " - " + "Computer score: " + str(cscore))
        
        if uscore == 3:
            print("Game over, you reign supreme over computers.")
        if cscore == 3:
            print("Game over, you must succub to technology.")
        
decide_winner()
            