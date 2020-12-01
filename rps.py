from random import *
items = ["ROCK", "PAPER", "SCISSORS"]
print("Welcome to the rock, paper, scissors thunderdome!")


rules = {"ROCK":"SCISSORS","PAPER":"ROCK","SCISSORS":"PAPER"}

scorecpu = 0
scoreplayer = 0

while scoreplayer < 5 and scorecpu < 5:
    player = ''
    while player not in items:
        player = input("Choose your rock, paper or scissors.").upper()
    print("You chose,", player)
    computer = choice(items)
    print("I chose,",computer)
    if player == computer:
        print("We drew")
    elif rules[player] == computer:
        scoreplayer = scoreplayer + 1
        print("You won this round, the score is:",scoreplayer,"for you and",scorecpu,"for me.")
    else:
        scorecpu = scorecpu + 1
        print("I won this round, the score is:",scoreplayer,"for you and",scorecpu,"for me.")

if scoreplayer == 5:
    print("fine, you beat me this time.... play again???")

if scorecpu == 5:
    print("boom zamaray! I beat you - I bet I can do it again")
