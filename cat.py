def prepend(listname, value):
    """The Clunky version"""
    listname.reverse()
    listname.append(value)
    listname.reverse()

def prepend2(listname, value):
    """The better version"""
    listname.insert(0,value)

def pycat(filename)
    txt = open(filename)
    print "Here's your file %r:" % filename
    print txt.read()
    txt.close()
