a = "test"
b = 'test'
c = 'test'

print "This is a %s." % a
print "This is a second %r." % a
print "Fuckin third %s." % b
print 'Hello fourth %r.' % c

d = "buttons"
e = 'wires'
print "I'm a \"computer\"."
print 'I\'m a clevery guy.'
print 'Everythin\' made out of \"%s\"...' % d
print '...and \"%r\".' % e

# %r prints it the way I wrote it in the atom file
# %s prints it the way I want it to look like

f = "\"Mister\""
g = "\"Mister\""

print "Hello %s" % f
print "Hello %r" % g
