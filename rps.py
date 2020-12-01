from random import *
items = ["ROCK", "PAPER", "SCISSORS"]
print("Welcome to the rock, paper, scissors thunderdome!")
player = ''
while player not in items:
    player = input("Choose your rock, paper or scissors.").upper()
print("You chose,", player)
computer = choice(items)
print("I chose,",computer)

rules = {"ROCK":"SCISSORS","PAPER":"ROCK","SCISSORS":"PAPER"}

if player == computer:
    print("We drew")
elif rules[player] == computer:
    print("You won")
else:
    print("I won!")
