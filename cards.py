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

numwords=["Zero", "One","Two","Three","Four","Five","Six","Seven",
		"Eight","Nine","Ten"]

card1=Card("Ace", "Hearts", "A")
card2=Card("Queen", "Clubs", "Q")

deck=[card1,card2]

print card1.showcard(),
print "(%s)" % card1.shortcard()

print "---"
