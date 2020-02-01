import random

user_wins = 0
comp_wins = 0

def User_Choise():
    user_choice = input("Rock, paper or scissors :")
    if user_choice in ["rock", "Rock", "R", "r"]:
        user_choice = "r"
    elif user_choice in ["paper", "Paper", "p", "P"]:
        user_choice = "p"
    elif user_choice in ["scissors", "scissor", "Scissors", "S", "s"]:
        user_choice = "s"
    else :
        print("Sorry i didn't understand, please try again");
        User_Choise()
    return user_choice

def Comp_Choice():
    comp_choice = random.randint(1,3)
    if comp_choice == 1:
        comp_choice = "r";
    elif comp_choice == 2:
        comp_choice = "p";
    else:
        comp_choice = "s";
    return comp_choice

while True:
    print("")
    user_choice = User_Choise()
    comp_choice = Comp_Choice()
    print("")

    if user_choice == "r":
        if comp_choice == "r":
            print("You chose rock. The computer chose rock. You tied.")
        elif comp_choice == "p":
            print("You chose rock. The computer chose paper. Computer wins.")
            comp_wins += 1
        elif comp_choice == "s":
            print("You chose rock. The computer chose scissors. You win.")
            user_wins += 1
    if user_choice == "p":
        if comp_choice == "r":
            print("You chose paper. The computer chose rock. You win.")
            user_wins += 1
        elif comp_choice == "p":
            print("You chose paper. The computer chose paper. You tied.")
        elif comp_choice == "s":
            print("You chose paper. The computer chose scissors. Computer wins")
            comp_wins += 1
    if user_choice == "s":
        if comp_choice == "r":
            print("You chose scissors. The computer chose rock. Computer wins")
            comp_wins += 1
        elif comp_choice == "p":
            print("You chose scissors. The computer chose paper. You win.")
            user_wins += 1
        elif comp_choice == "s":
            print("You chose scissors. The computer chose scissors. You tied.")

    print("")
    print("Player wins: " + str(user_wins))
    print("Computer wins: " + str(comp_wins))
    print("")

    if user_wins == 3:
        print("You won the match!")
        print("")
        print("This game has been coded by Impterium, if you want to contact me this is my discord tag Imperium#0543")
        user_ask = input("Do you want to play again? (y/n)")
        if user_ask in ["y", "Yes", "yes", "Y"]:
            pass
            comp_wins = 0
            user_wins = 0
        elif user_ask in ["no", "No", "N", "n"]:
            break
        else:
            break
    if comp_wins == 3:
        print("Computer won!")
        user_ask = input("Do you want to play again? (y/n)")

        if user_ask in ["y", "Yes", "yes", "Y"]:
            pass
            comp_wins = 0
            user_wins = 0
        elif user_ask in ["no", "No", "N", "n"]:
            break
        else:
            break
