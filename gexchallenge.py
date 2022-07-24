import re

f = open('BLR Flight Schedule.csv', 'r')
out = open('output.txt', 'w')

departures = []
f.readline()

for s in f.readlines():
    if(re.search('Departure', s)):
        departures.append(s)

for s in departures:
    info = re.findall(r'(^\d\d-\d\d-\d\d\d\d),(\w+ \w+),([\w | ]+),.*,[A-Z]{3},([\w | ]+)', s)
    infoTuple = info[0]
    date, flightno, airline, destination = infoTuple
    out.write("Bangalore --[" + airline + ": " + flightno + "]--> " + destination + ": " + date + "\n")
    
f.close()
