# Zoe Valladares
# CISC320 - SP2022
# Cow! Algo Problem

'''
ok lets think about this:
- the last element is the time stamp 
--- we can use this are the sorting "key"
--- use an integrated sorting algo to take the last 
element of the string/list/dicitionary (figure this out later)
and sort the file

- then we need to check for a "M", "W", or "T"
.split(" ") is a good choice

with open('test.txt') as f:
    cows = dict(i.strip().split(None, 1) for i in f)
print(cows)
dict = {}
with open('test.txt') as data_file:
    for line in data_file:
        (key, action, value, time) = line.split(" ")
        dict[int(key)] = value

print(dict)
'''
import json
filename = 'test.txt'
COWS = {}
fields = ['cowID', 'action', 'value', 'time']

with open(filename) as f_op:
    count = 1
    for line in f_op:
        description = list(line.strip().split(None, 4))
        print(description)
        sno = 'cow'+str(count)
        i = 0
        dict1 = {}
        while i<len(fields):
            dict1[fields[i]] = description[i]
            i = i + 1
        COWS[sno] = dict1
        count = count + 1
        #command, description = line.strip().split(None, 1)
        #COWS[command] = description.strip()

out_file = open("test.json", "w")
json.dump(COWS, out_file, indent = 4, sort_keys = False)
out_file.close()
