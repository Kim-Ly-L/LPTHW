from sys import argv

# variable "filename" to get a filename
script, filename = argv

# parameter = function(own variable)
# function => returns a value/ picks a file
txt = open(filename)

print "Here's your file %r:" % filename
# command for the opened file
# Give the command by using the file name; . (dot); name of the...
# ...command; parameters (when given)
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
