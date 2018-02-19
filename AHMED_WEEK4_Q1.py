#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 11:22:46 2018

@author: Aslan
"""

from enum import Enum
import numpy as np
class CoinGame(Enum): # State of each coin toss
    HEADS = 1
    TAILS = 0

class Game: #create cointoss game
    def __init__(self):
        self._probabilityofheads = headprobability #Heads?
        self._CoinGame = [] #Whst's the winning outcome?
        self._superresult = [] #All toss outcome
        self._rnd = np.random #randomizer!
        #note: you'll get a diff result every time b/c randomized tosses.

    def simulate(self, numberoftosses):
        numberoftosses = 20
        headprobability = 0.5
        t = 0
        while t < numberoftosses:

            if self._rnd.sample() < self._probabilityofheads:
                self._CoinGame = CoinGame.HEADS
            else:
                self._CoinGame = CoinGame.TAILS #it's a bindary

            self._superresult.append(self._CoinGame.name)
            t += 1 #add a toss



    def tally(self):
        reward = 100
        initialbuyin = 250
        addedwins = " ".join(map(str,self._superresult))
        TTH = "TAILS TAILS HEADS"
        winnumber = addedwins.count(TTH)
        totalcost = (winnumber*reward)-(initialbuyin)
        #this formula can help us get an avg payout
        return totalcost
    #superresult is your coin toss outcome. Total cost is your payout outcome.

print ("This is a self-check. The probs of heads is...", headprobability)
print ("This is a self-check. The # of tosses per round is...", numberoftosses)

class Rounds:
    def __init__(self, rounds):
        self.Rounds = rounds
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
            game.simulate(numberoftosses) #initiate cointoss from the simulation model
            outcome = game.tally()
            self.tallytotal.append(outcome)

    def totalavgcost(self):
        return sum(self.tallytotal)/ len(self.tallytotal)

myRounds = Rounds(numberofrounds)
numberofrounds = 1000
myRounds.playagame()
print ("This is a self-check. The # of rounds is...", numberofrounds)
print("\n____________________________\n")


print("With an initial buyin of...", initialbuyin, "USD$")
print("And a reward for a TAIL-TAILS-HEAD sequence being...", reward, "USD$")
print("Out of a total of...", numberofrounds, "rounds")
print("With...", numberoftosses, "tosses per round")
print("The expected payout from this game is...", myRounds.totalavgcost(), "USD$")
