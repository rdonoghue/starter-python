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


def filldeck():
    '''creates a deck of cards (non manipulable)'''
    mydeck=[];
    suits=["clubs", "diamonds", "hearts", "spades"]
    faces=["Jack","Queen","King","Ace"]
    for suit in suits:
        for num in range(2,11):
            card="%s of %s" % (num, suit)
            mydeck.append(card)
        for face in faces:
            card="%s of %s" % (face, suit)
            mydeck.append(card)
    return mydeck

def shuffledeck(sdeck):
    '''Randomly Reorders the Deck (or any list)
    pretty much crap. Badly need a different procedure.'''
    cards=len(sdeck)
    print cards,"cards"
    for events in range(0,cards):
        pos=0
        for marker in sdeck:
            flip=random.randint(1,2)
            if flip == 1:
                npos=pos+1
                if pos==cards - 1:
                    npos=-1
                sdeck[pos],sdeck[npos] = sdeck[npos],sdeck[pos]
            pos += 1
    return sdeck

def dealcards(handsize):
    thisdeck=filldeck()
    thisdeck=shuffledeck(thisdeck)
    thishand=[]
    for draws in range(0,handsize):
        thishand.append(thisdeck.pop(0))
    return thishand


smalldeck=["Foo", "bar", "baz", "red", "white", "blue"]

#random NUmber, inclusive
print roll(3,6)

#Pick one from a list
stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]
print random.choice(stuff)

deck = filldeck()
print "You drew the", random.choice(deck)

# newdeck=shuffledeck(deck)

newdeck=shuffledeck(smalldeck)

for cards in newdeck:
    print cards


myhand = dealcards(5)
myhand.sort()
print myhand



## And now for functions!
number_of_rolls=3
die_size=6
rolls=5000000

# myrolls=rollarray(number_of_rolls,die_size,rolls)
# print myrolls

# getdicecurve(number_of_rolls,die_size,myrolls)


# print graph

#for foo in range(2,13):
#    print foo,
#    print "\t",
#    myval=percent(graph[foo],rolls)
#    print myval,"%s" % literalpercent
#    for holder in range(0,graph[foo]):
#        print "*",
