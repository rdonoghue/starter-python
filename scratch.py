def filldeck():
	mydeck=[]
	suits=["clubs", "diamonds", "hearts", "spades"]
	faces=["Jack","Queen","King","Ace"]
	   for suit in suits:
			for num in range(2,11):
			card=num, suit of %s" % (num, suit,numwords[num])
			mydeck.append(card)
		for face in faces:
			card="%s of %s" % (face, suit)
			mydeck.append(card)
	return mydeck
