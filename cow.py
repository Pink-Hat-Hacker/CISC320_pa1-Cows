# Zoe Valladares
# CISC320 - SP2022
# Cow! Algo Problem

'''
test_file = open('test.txt', 'r')
content = test_file.read()
print(content)
test_file.close()
'''

'''
ok lets think about this:
- the last element is the time stamp 
--- we can use this are the sorting "key"
--- use an integrated sorting algo to take the last 
element of the string/list/dicitionary (figure this out later)
and sort the file

- then we need to check for a "M", "W", or "T"
.split(" ") is a good choice
'''
with open('test.txt') as f:
    cows = dict(i.strip().split(None, 1) for i in f)
print(cows)