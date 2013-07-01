# import the argv module
from sys import argv

# set the variables that will be passed by argv
script, filename = argv

# open the file 'filename'
txt = open(filename)

print "Here's your file %r:" % filename
# read the file you have opened and print it to the screen
print txt.read()
txt.close()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)
print txt_again.read()
txt_again.close()

a = txt_again.closed
print "Is the file closed? %r" % a
