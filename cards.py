import random

class Card(object):
	"""Playing cards as a class"""
	def __init__(self,face,suit,value):
		self.face = face
		self.suit = suit
		self.value = value
	def showcard(self):
		return "%s of %s" % (self.face, self.suit)
	def shortcard(self):
		if self.suit == "Hearts":
			ssuit= "H"
		elif self.suit == "Diamonds":
			ssuit= "D"
		elif self.suit == "Clubs":
			ssuit= "C"
		elif self.suit == "Spades":
			ssuit= "S"
		else:
			ssuit="?"
		return "%s%s" % (self.value, ssuit)

def filldeck():
	mydeck=[]
	suits=["clubs", "diamonds", "hearts", "spades"]
	faces=["Jack","Queen","King","Ace"]
	numwords = [
	"Zero", "One", "Two", "Three",
	"Four","Five", "Six", "Seven",
	"Eight","Nine","Ten"
	]
	for suit in suits:
		for num in range(2,11):
			card = Card(num, suit,numwords[num])
			mydeck.append(card)
		for face in faces:
			if face == "Jack":
				sface="J"
			elif face == "Queen":
				sface="Q"
			elif face == "King":
				sface="K"
			elif face == "Ace":
				sface="A"
			else:
				sface="?"
			card = Card(face, suit,sface)
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

card1=Card("Ace", "Hearts", "A")
card2=Card("Queen", "Clubs", "Q")

deck=[card1,card2]

print card1.showcard(),
print "(%s)" % card1.shortcard()

print "(%s)" % deck[1].shortcard()

print "---"

classdeck=filldeck()

print classdeck[0].showcard()
print len(classdeck)
classdeck=shuffledeck(classdeck)
myhand=dealcards(5)
for card in myhand:
	print card.showcard()
