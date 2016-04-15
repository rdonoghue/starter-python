import random

class Card(object):
	"""Playing cards as a class"""
	def __init__(self,face,suit,value,short_suit):
		self.face = face
		self.suit = suit
		self.value = value
		self.short_suit = short_suit
	def showcard(self):
		return "%s of %s" % (self.face, self.suit)
	def shortcard(self):
		return "%s%s" % (self.value, self.short_suit)

def filldeck():
	mydeck=[]
	faces=["Jack","Queen","King","Ace"]
	faces={"Jack":"J","Queen":"Q","King":"K","Ace":"A"}
	numwords = [
	"Zero", "One", "Two", "Three",
	"Four","Five", "Six", "Seven",
	"Eight","Nine","Ten"
	]
	suitnames={"Hearts":"H","Diamonds":"D","Clubs":"C", "Spades":"S"}
	for suit in suitnames:
		for num in range(2,11):
			card = Card(numwords[num], suit,num,suitnames[suit])
			mydeck.append(card)
		for face in faces:
			card = Card(face, suit,faces[face],suitnames[suit])
			mydeck.append(card)
	return mydeck

def shuffledeck(sdeck):
    '''Randomly Reorders the Deck (or any list).  This is brute force and not very good'''
    cards=len(sdeck)
    print "Shuffling",cards,"cards"
    for events in range(0,cards * 100):
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

card1=Card("Ace", "Hearts", "A", "H")
card2=Card("Queen", "Clubs", "Q", "C")

deck=[card1,card2]

#print card1.showcard(),
#
#print "(%s)" % deck[1].shortcard()

print "---"

classdeck=filldeck()

# Draw one card
drawncard=random.choice(classdeck)
print "Drew the %s (%s)." % (drawncard.showcard(), drawncard.shortcard())

print "---"
'''
print classdeck[0].showcard()
print len(classdeck)
classdeck=shuffledeck(classdeck)
myhand=dealcards(5)
for card in myhand:
	print card.showcard()
'''
