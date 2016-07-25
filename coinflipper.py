#init the coin flip
#repeat it ten times
#flip a bool statement if a coin flips ten times
#use an if statement to check whether one coin flipped
#compare successful runs over total runs
import numpy as np
headortail = np.array([1,2])
class coin(object):
    def __init__(self,checkheads=0):
     self.checkheads = checkheads   
    def coinflip(self, number):
        for i in range(0,number):
         coinz = np.random.choice(headortail)
         if coinz == 1:
             self.checkheads = self.checkheads + 1
        return self.checkheads
    
class arrayofcoins(object):
    def __init__(self, number):
        self.number = number
    def successnumber(self):
        for x in range(0,self.number):
            coinx = coin()
            if coinx.coinflip(10) == 10:
                return 1
                del coinx
                break
            else:
                del coinx
                
class dirtyworkdoer(object):
    def __init__(self, trials):
        self.trials = trials
        self.successruns = 0
    def probability(self):
     batcoins = arrayofcoins(1000)
     for m in range(0,self.trials):
         if batcoins.successnumber() == 1:
          self.successruns = self.successruns + 1
     return float(self.successruns) / self.trials

calculatedprobability = 1 - (1 -(0.5) ** 10) ** 1000
comp = dirtyworkdoer(input("input number of trials"))
a = comp.probability()
print "probability is", a
print "analytical probability is ", calculatedprobability            
            
#calculatedprobability = float(0)

#successruns = int(0)
#successcount = int(0)
#totalruns = int(input("input number of runs you want"))
#checkheads = int(0)
#calculatedprobability = 1 - (1 -(0.5) ** 10) ** 1000
#for z in range (0, totalruns):
# for x in range (0, 1000):
#  for i in range (0, 10):
#   coin = np.random.choice(headortail)
#   if coin == 1:
#        checkheads = checkheads + 1
#  if checkheads == 10:
#     successcount = successcount + 1
#  checkheads = 0
# if successcount >= 1:
#  successruns = successruns + 1
# successcount = 0
#probability = float(successruns) / totalruns
#print "probability is", probability
#print "successful runs are", successruns
#print "calculated probability is", calculatedprobability
        
    












































