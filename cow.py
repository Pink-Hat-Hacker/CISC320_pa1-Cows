# Zoe Valladares
# CISC320 - SP2022
# Cow! Algo Problem

class Cow:
    def __init__(self, id, a, v):
        self.cowid = id
        self.action = a
        self.value = v

filename = 'test.txt'
COWS = {}
count = 0
with open(filename) as f_op:
    for line in f_op:
        data = list(line.strip().split(None, 4))
        COWS[line[0]] = data
        print(data[0] + " " + data[1] + " " + data[2])

print(COWS)