# The function; it's gonna take in all the following arguments:

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

# First argument
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# Second argument (a little bit annoying though since it's extra work...
# ... in comparison to l.11)
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Math, not much to add to that
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# Okay that's interesting,apparently, the function can combine arguments...
# ... or take information from a previous arg to implement the new arg
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
