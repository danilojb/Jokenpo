import random

def get_choices():
  player_choice = input("Enter a choice (rock, paper, scissors: )")
  computer_options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(computer_options)
  choices = {"player": player_choice, "computer": computer_choice}
  #return player_choice
  return choices

choices = get_choices()
print(choices)