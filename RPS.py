import random
import time

# idk why i put this in a function


def Game():
    print("Welcome to Rock, Paper, Scissors")
    print("First to 3 wins is the ultimate winner")
    time.sleep(2)
    userWins = 0
    compWins = 0
    while (userWins <= 2 and compWins <= 2):
        user_input = input(
            "Please enter Rock, Paper or Scissors(Case Sensitive): ")
        print("You have chosen "+user_input)
        time.sleep(2)
        comp_out = "Rock", "Paper", "Scissors"
        comp_out = random.choice(comp_out)
        print("The computer has chosen "+comp_out)
        time.sleep(2)
# Draw
        if(user_input == comp_out):
            print("It's a Draw")
# User Wins
        if(user_input == "Rock" and comp_out == "Scissors"):
            print("You win")
            userWins = userWins + 1
        elif(user_input == "Paper" and comp_out == "Rock"):
            print("You win")
            userWins = userWins + 1
        elif(user_input == "Scissors" and comp_out == "Paper"):
            print("You win")
            userWins = userWins + 1
# Computer Wins
        elif(user_input == "Scissors" and comp_out == "Rock"):
            print("Computer Wins")
            compWins = compWins + 1
        elif(user_input == "Rock" and comp_out == "Paper"):
            print("Computer Wins")
            compWins = compWins + 1
        elif(user_input == "Paper" and comp_out == "Scissors"):
            print("Computer Wins")
            compWins = compWins + 1

    time.sleep(2)
    print("==============")
    time.sleep(2)
    print("Computer Score: "+str(compWins))
    print("Your Score: "+str(userWins))
    print("==============")
    time.sleep(2)
    if (compWins > userWins):
        print("The Compter Is The Ultimate!!!(you suck)")
    elif (compWins < userWins):
        print("You Are The Ultimate Winner!!!")
    else:
        print("It's a Draw")
    playAgain = input(("Would you like to play again?(y or n): "))
    if (playAgain == 'y'):
        Game()
    else:
        print("Okay Goodbye")


Game()
