# Here's some new strange stuff, remember type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"
# when it comes to "\n" the kind of the slash does play a role!
# even on Windows
# "\n" separates the terms/characters within a string into different lines
# ...even though there's no spacing - magic!
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

# 11 & 12: There need to be a space after the ":"
# otherwise the days/months would be printed  right afterwards without any space
# it would look ugly
print "Here are the days: ", days
print "Here are the months: ", months

print """""""""""""""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""""""""""""""
