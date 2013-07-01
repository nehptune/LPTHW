# a simple script to calculate which plates are needed to load 215lb onto
# a barbell using standard plates

print "how many plates are needed to load 215lbs onto a barbell?"

print "how much weight is needed once the 45lb barbell is accounted for?"
a=215-45
print a

# do we need to use the largest, 45lb plates? only if a > 45*2
print "do we need to use the largest plates?" 

if a > 45*2:
    print "yes"
else:
    print "no"
    
b = a - 45*2

# now which plates do we need? b is the remaining weight after the barbell
# and the 2 45lb plates
# the remaining weight needed either side is b/2.

print "how much weight do we need to load either side of the barbell now?"
c = b/2.
print c

print "do we need 25lb plates?" 

if c >= 25:
    print "yes"
else:
    print "no"

# how much weight is needed after adding 25lb plates?
d = c - 25
print "how much weight is still needed?" , d



