from sys import argv
from os.path import exists
# One can squeeze different lines into one line by using ";"
script, from_file, to_file = argv
in_file = open(from_file)
indata = in_file.read()
out_file = open(to_file, 'w')
out_file.write(indata)

# alternatively write: indata = open(from_file).read() etc.

print "Alright, all done."

out_file.close()
in_file.close()
