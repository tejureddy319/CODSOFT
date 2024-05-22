import random
def determine_winner(user_choice,computer_choice):
    if user_choice==computer_choice:
        return "It is tie!"
    elif (user_choice=="rock" and computer_choice=="scissors")or(user_choice =="scissors" and computer_choice=="paper")or(user_choice=="papaer" and computer_choice=="rock"):
        return "You win!"
    else:
        return "computer wins!"


def play_round():
    user_choice=input("choose rock,paper,scissors:").lower()
    computer_choice=random.choice(["rock","paper","scissors"])
    print("computer chooses:",computer_choice)
    print(determine_winner(user_choice,computer_choice))


def play_game():
    play_again=True
    user_score=0
    computer_score=0
    while play_again:
        play_round()
        user_input=input("Do u want to play again?(y/n):").lower()
        if user_input!="y":
            play_again=False

    print("Final score:")
    print("you:",user_score)
    print("computer:",computer_score)

play_game()
                         
                                   
