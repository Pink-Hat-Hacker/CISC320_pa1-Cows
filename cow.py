# Zoe Valladares
# CISC320 - SP2022
# Cow! Algo Problem

import sys

class Cow:
    #ids, lateW, lowW, avgM, totalM, numM, currTime = 0

    def __init__(self, ids):
        #needs to be output
        self.cowid = ids
        self.lateW = 0
        self.lowW = sys.maxint
        self.avgM = 0
        #needd for calc data
        self.totalM = 0
        self.numM = 0
        self.currTime = 0

    def __repr__(self):
        #return "[CowID: %s, LowestW: %s, LatestW: %s, AvgM: %s]" % (self.cowid, self.lowW, self.lateW, self.avgM)
        return "[%s, %s, %s, %s]" % (self.cowid, self.lowW, self.lateW, self.avgM)
    
    #basically java getters and setters bbc i cant choose a language
    #Milk
    def addNumMilk(self):
        self.numM = self.numM + 1
        #print(self.numM)
    def setTotalM(self, totalM):
        self.totalM += totalM
        #print(self.totalM)
    def setAvgM(self):
        self.avgM = self.totalM / self.numM
    
    #Time
    def getLatestTime(self):
        return self.currTime
    def setTimeLatest(self, currTime):
        self.currTime = currTime

    #Weight
    def setLatestW(self, lateW):
        self.lateW = lateW
    def getLowestW(self):
        return self.lowW
    def setLowestW(self, lowW):
        self.lowW = lowW
    #ig i need a getID key thing bc i cant figure this out!!!
    def getID(self):
        return self.id

filename = 'test.txt'

#cow dictionary
COWS = {}
#fields
data = []
ids = 0
action = ""
value = 0
time = 0
count = 0
def getKeys(dict, key):
    if key in dict.keys():
        return True
    return False

with open(filename) as f_op:
    #loop through file and getID each line of data 
    for line in f_op:
        #data of each line 
        data = list(line.strip().split(None, 4))
        ids = int(data[0])
        action = data[1]
        value = int(data[2])
        time = int(data[3])
        #print(time)

        #check if key is not contained in dict
        if not(getKeys(COWS, ids)):
            COWS[ids] = Cow(ids)
            #print(COWS[ids])
        if action == "M":
            COWS[ids].addNumMilk()
            COWS[ids].setTotalM(value)
            COWS[ids].setAvgM()
        elif action == "W":
            if time > COWS[ids].getLatestTime():
                COWS[ids].setTimeLatest(time)
                COWS[ids].setLatestW(value)
            if value < COWS[ids].getLowestW():
                COWS[ids].setLowestW(value)
#make sure to close the file!!!

#sorting O(nlog(n))

print(COWS)