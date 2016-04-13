def prepend(listname, prepend_value):
    '''Reverses the list, appends the new value, then reverses it again.
    Clunky and ungraceful, but it works until I find a really way to
    prepend'''
    listname.reverse()
    listname.append(prepend_value)
    listname.reverse()




from sys import argv
filename = argv[1]
# filename = "textfile.txt"
txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

txt.close()
