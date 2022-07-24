import re

f = open('BLR Flight Schedule.csv', 'r')

departures = []
f.readline()

for s in f.readlines():
    if(re.search('Departure', s)):
        departures.append(s)

for s in departures:
    info = re.findall(r'(^\d\d-\d\d-\d\d\d\d,\w+ \w+,[\w | ]+,)Departure,BLR,Bengaluru,Kempegowda International Airport,\d\d-\d\d-\d\d\d\d,\d\d:\d\d .*,(?: \d\d:\d\d .*)?,\d?,\w\w\w,([\w | ]+)', s)
    print(info)
    
f.close()
