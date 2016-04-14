import random

def percent(v1,v2):
    value1 = v1 * 1.0
    value2 = v2
    percentage = ((value1 * 100)/value2)
    return  percentage

def roll(d1,d2):
    '''Rolls XdX dice, Require random'''
    value=0
    for n in range(0,d1): # This many dice
        value +=int(random.randint(1,d2))
    return value

def rollarray(d1,d2,repeat):
    minval = d1
    maxval = d1 * d2
    dicearray=[]
    for z in range(0,maxval+1): # fill with Zeros
        dicearray.append(0) # Must be a better way
    for z in range(0,repeat):
        val = int(roll(d1,d2))
        dicearray[val]= dicearray[val] + 1
    return dicearray

def getdicecurve(minval,maxval,dicelist):
    print dicelist
    for foo in range(minval,(minval * maxval)+1):
        myrolls=(sum(dicelist) * 1.0)
        myval=percent(dicelist[foo],myrolls)
        print "%s\t%.1f%%" % (foo,myval)


#random NUmber, inclusive
print roll(3,6)

#Pick one from a list
stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]
print random.choice(stuff)


## And now for functions!
number_of_rolls=3
die_size=6
rolls=5000000

myrolls=rollarray(number_of_rolls,die_size,rolls)
print myrolls

getdicecurve(number_of_rolls,die_size,myrolls)


# print graph

#for foo in range(2,13):
#    print foo,
#    print "\t",
#    myval=percent(graph[foo],rolls)
#    print myval,"%s" % literalpercent
#    for holder in range(0,graph[foo]):
#        print "*",
