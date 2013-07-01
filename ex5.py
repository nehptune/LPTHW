name = 'Sophie A. Clayton'
age = 33 # not a lie!
height = 68 # inches
weight = 146 # lbs, not a lie either
eyes = 'Blue'
teeth = 'White'
hair = 'Red'

print "Let's talk about %s." % name
print "She's %d inches tall." % height
print "She's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "She's got %s eyes and %s hair." % (eyes, hair)
print "Her teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d and %d I get %d." %(
    age, height, weight, age + height + weight)

# now convert the height and weight to metric (cm and kg)
conv_cm = 2.54
conv_kg = 0.454

print "She weighs %d kilograms" % (weight * conv_kg)
print"And she is %f cms tall" % (height * conv_cm)
