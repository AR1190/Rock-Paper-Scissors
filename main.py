import random

computerOptions = ["Rock", "Paper", "Scissors"]
computerChoice = computerOptions[random.randint(0,2)]

print("Welcome to Rock, Paper, Scissors")

userChoice = input("Choose your weapon: ")

if(computerChoice == "Rock" and userChoice == "Paper"):
  print("You won!I chose Rock")
elif(computerChoice == "Paper" and userChoice == "Rock"):
  print("You lost! I chose Paper")
  