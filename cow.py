# Zoe Valladares
# CISC320 - SP2022
# Cow! Algo Problem

import sys

class Cow:
    def __init__(self, id):
        #needs to be output
        self.cowid = id
        self.lateW = 0
        self.lowW = sys.maxint
        self.avgM = 0
        #calc data
        self.totalM = 0
        self.numM = 0

    def __repr__(self):
        #return "[CowID: %s, LatestW: %s, LowestW: %s, AvgM: %s]" % (self.cowid, self.lateW, self.lowW, self.avgM)
        return "[%s, %s, %s, %s]" % (self.cowid, self.lateW, self.lowW, self.avgM)
    
    #basically java getters and setters bbc i cant choose a language

    
    


filename = 'test.txt'

#cow dictionary
COWS = {}
#fields
data = []
ids = 0
action = ""
value = 0


with open(filename) as f_op:
    #loop through file and get each line of data 
    for line in f_op:
        #data of each line 
        data = list(line.strip().split(None, 4))
        ids = int(data[0])
        action = data[1]
        value = data[2]

        #check if key is not contained in dict
        if not(ids in COWS.keys()):
            COWS[line[0]] = Cow(ids)
        if action == "M":
            COWS.key(ids).addNumMilk()
            COWS.key(ids).setTotalM()
            #COWS.key(ids).setAvgM()
        elif action == "W":
            if time > COWS.key(ids).getLatestTime():
                COWS.key(ids).setTimeLatest(time)
                COWS.key(ids).setLatestW(value)
            if value < COWS.key(ids).getLowestWeight():
                COWS.key(ids).setLowestW(value)
print(COWS)