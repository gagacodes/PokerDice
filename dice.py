import random


class dice:

    def roll(self):
        dice = [9, 10, 'Jack', 'Queen', 'King', 'Ace']
        n = random.randint(0, 5)
        n1 = random.randint(0, 5)
        n2 = random.randint(0, 5)
        n3 = random.randint(0, 5)
        n4 = random.randint(0, 5)
        dice_5 = [dice[n], dice[n1], dice[n2], dice[n3], dice[n4]]
        print(str(dice_5) + "\n")
        n = 0
        t = 0
        j = 0
        q = 0
        k = 0
        a = 0
        for i in dice_5:
            if i == 9:
                n += 1
            elif i == 10:
                t += 1
            elif i == 'Jack': 
                j += 1
            elif i == 'Queen':
                q += 1
            elif i == 'King':
                k += 1
            elif i == 'Ace':
                a += 1
        #print(n, t, j, q, k, a)
        self.score = 0
        if [n,t,j,q,k,a].count(3) == 1 and [n,t,j,q,k].count(2) == 1:
            print("You got a full house!")
            self.score += 6
        elif [n,t,j,q,k,a].count(3) == 1:
            print("You got 3 of a kind!")
            self.score += 4
        elif [n,t,j,q,k,a].count(4) == 1:
            print("You got 4 of a kind!")
            self.score += 7
        elif [n,t,j,q,k,a].count(5) == 1:
            print("You got 5 of a kind!")
            self.score += 8
        elif [n,t,j,q,k,a].count(2) == 2:
            print("You got 2 pair")
            self.score += 3
        elif [n,t,j,q,k,a].count(2) == 1:
            print("You got 1 pair")
            self.score += 2
        elif [t,j,q,k,a].count(1) == 5 or [n,t,j,q,k].count(1) == 5:
            print("You got a straight!")
            self.score += 5
        else:
            print("Bust")
            self.score += 0
        

        


    
        