
import random
from dice import *
from player import *

p = player()

running = True



playerStart = str.lower(input("""Welcome to Gage Ward's Artisanal Poker Dice.
Type start if you'd like to play!
"""))
if(playerStart == "start"):
    running = True
else:
    print('thanks for playing!')
    running = False

cpuScore = 0 
playerScore = 0

while running:
    p.playerRoll()
    print(p.aggragateScorePlayer)
    p.cpuRoll()
    print(p.aggragateScoreCpu)
    if p.aggragateScoreCpu > p.aggragateScorePlayer:
        print("The Computer won this hand!")
        cpuScore += 1
    elif p.aggragateScoreCpu < p.aggragateScorePlayer:
        print("You won this hand!")
        playerScore += 1
    else:
        print("You Tied. :(")
    print("Your score - ", playerScore, " Computer's score", cpuScore)
    if cpuScore == 11:
        print("""Computer won!
""")
        running = False
    elif playerScore == 11:
        print("""You won!!
""")
        running = False

print("Thanks for playing Gage's Artisanal Poker Dice!")