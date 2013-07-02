from sys import argv

script, filename = argv

target = open(filename,'r')
txt = target.read()

print """
This is your file: %s
""" % txt


