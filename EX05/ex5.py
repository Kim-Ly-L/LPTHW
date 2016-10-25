name = 'Zed A. Shaw'
age = 35.0 # not a lie
height = 74.0 * 2.54 # inches to cm
weight = 180.0 * 0.453592 # lbs to kg
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %f centimeters tall." % height
print "He's %f kilograms heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

#this line is tricky
print "If I add %f, %f, and %f I get %f." % (
age, height, weight, age + height + weight)
