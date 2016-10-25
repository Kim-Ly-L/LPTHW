x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke funny?! %r"

print joke_evaluation % hilarious
#notice: after print there's no '=' (equal)

w = "This is the left side of..."
e = "a string with a right side."

print w + e
# 21 makes a longer string than:
# print w
# print e
#... because it adds both strings together
