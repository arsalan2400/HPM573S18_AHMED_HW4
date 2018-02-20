from enum import Enum
import numpy as np

class CoinGame(Enum):
    TAILS = 0
    HEADS = 1

class Game: #create cointoss game
    def __init__(self):
        self._probabilityofheads = headprobability #Heads?
        self._CoinGame = [] #What's the winning outcome?
        self._superresult = [] #All toss outcome
        self._rnd = np.random #it's a randomizer!note: you'll get a diff result every time b/c randomized tosses.


    def simulate(self, numbertosses):
        t = 0
        while t < numbertosses:
            if self._rnd.sample() < self._probabilityofheads:
                self._CoinGame = CoinGame.HEADS
            else:
                self._CoinGame = CoinGame.TAILS #it's a binary
            self._superresult.append(self._CoinGame.name)
            t += 1 #add a toss


    def tally(self):
        reward = 100
        addedwins = " ".join(map(str,self._superresult))
        TTH = "TAILS TAILS HEADS"
        winnumber = addedwins.count(TTH)
        totalcost = (winnumber*reward)-(initialbuyin)
        #this formula can help us get an avg payout
        return totalcost
    #superresult is your coin toss outcome. Total cost is your payout outcome.

headprobability = 0.4
initialbuyin = 250
numbertosses = 20
print("This is a self-check. The reward for TAIL-TAILS-HEAD sequence is...", reward, "USD$")
print ("This is a self-check. The probs of heads is...", headprobability)
print ("This is a self-check. The # of tosses per round is...", numbertosses)

class therounds:
    def __init__(self, rounds):
        self.therounds = rounds
        self.supergames = []
        for i in range(rounds):
            game = Game()
            #link it back 2 the other class
            self.supergames.append(game)
            #add score of rounds together

        self.tallytotal = []


    def playagame(self):
        #all of these sourcing from Game() that class way up in the code's beginning
        #it lets us tap into our simulation model
        for game in self.supergames:
            #better defining supergames
            game.simulate(numbertosses) #initiate cointoss from the simulation model
            outcome = game.tally()
            self.tallytotal.append(outcome)

    def totalavgcost(self):
        return sum(self.tallytotal)/ len(self.tallytotal)

numberofrounds = 1000
these_rounds = therounds(numberofrounds)
these_rounds.playagame()


print ("This is a self-check. The # of rounds is...", numberofrounds)
print("____________________________\n")


print("With an initial buyin of...", initialbuyin, "USD$")
print("The expected payout from this game is...", these_rounds.totalavgcost(), "USD$")
