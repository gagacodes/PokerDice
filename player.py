import random

from dice import *

a = dice()
b = dice()
c = dice()

aCpu = dice()
bCpu = dice()
cCpu = dice()
class player:



    def cpuRoll(self):
        self.aggragateScoreCpu = 0
        print("Computer's Roll:")
        aCpu.roll()
        bCpu.roll()
        cCpu.roll()
        self.aggragateScoreCpu = aCpu.score + bCpu.score + cCpu.score
        
    def playerRoll(self):
        self.aggragateScorePlayer = 0
        firstRoll = str.lower(input("""Would you like to roll?
"""))
        if firstRoll == "yes":
            print("Your Roll:")
            a.roll()
            
            b.roll()
            
            c.roll()
            
            self.aggragateScorePlayer = a.score + b.score + c.score
        else:
            print("your turn will be skipped")
