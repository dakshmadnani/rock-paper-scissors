import random
def user_choice():
    player_choice=input("Enter one of the choices(rock,paper,scissors): ")
    option=["rock","scissors","paper"]
    computer_choice=random.choice(option)
    choices={"What you chose": player_choice,"What the computer chose": computer_choice}
    return choices
    
output=user_choice()
print(output)

def who_won(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Draw, try again."
    elif player_choice == "rock" and computer_choice == "paper":
        return "You lose."
    elif player_choice == "rock" and computer_choice == "scissors":
        return "You win."
    elif player_choice == "paper" and computer_choice == "rock":
        return "You win."
    elif player_choice == "paper" and computer_choice == "scissors":
        return "You lose."
    elif player_choice == "scissors" and computer_choice == "rock":
        return "You lose."
    elif player_choice == "scissors" and computer_choice == "paper":
        return "You win."

result = who_won(output["What you chose"], output["What the computer chose"])

print(result)