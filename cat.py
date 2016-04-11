from sys import argv
filename = argv[1]
# filename = "textfile.txt"
txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()
