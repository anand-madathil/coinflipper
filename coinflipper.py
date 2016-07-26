"""
init the coin flip
repeat it ten times
flip a bool statement if a coin flips ten times
use an if statement to check whether one coin flipped
compare successful runs over total runs
"""
import numpy as np
headortail = np.array(["heads","tails"])
class coin(object): 
    """coin object with the flip function"""
    def __init__(self,checkheads=0):
        self.checkheads = checkheads   
    def coinflip(self, number):
        """random variable coinz to store values for heads or tails"""
        for i in range(0,number):
            coinz = np.random.choice(headortail)
            if coinz == "heads":
                self.checkheads = self.checkheads + 1
        return self.checkheads 
        """checkheads returns number of heads"""

class arrayofcoins(object): 
    """stacks multiple coins to form the group required for the problem"""
    def __init__(self, number):
        self.number = number
    def successnumber(self): 
        """creates the coin flipping run. If one coin gets flipped correctly ten times no point continuing as regardless of the rest of the outcomes the output is 1, so break"""
        for x in range(0,self.number):
            coinx = coin()
            if coinx.coinflip(10) == 10:
                return 1
                del coinx
                break
            else:
                del coinx

class dirtyworkdoer(object): 
    """the object which actually flips the coins and calculates the practical probability"""
    def __init__(self, trials):
        self.trials = trials
        self.successruns = 0
    def probability(self): 
        """does the multiple runs required, and gives a float number for practical probability"""
        batcoins = arrayofcoins(1000) #code can be messed with to make a custom value for x in arrayofcoins(x), but theoretical probability calculation must also be changed
        for m in range(0,self.trials):
            if batcoins.successnumber() == 1:
                self.successruns = self.successruns + 1
        return float(self.successruns) / self.trials

calculatedprobability = 1 - (1 -(0.5) ** 10) ** 1000
comp = dirtyworkdoer(input("input number of trials"))
a = comp.probability()
print "probability is", a
print "analytical probability is ", calculatedprobability            
















































