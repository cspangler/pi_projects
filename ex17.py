from sys import argv
from os.path import exists

script, from_file, to_file = argv
prompt = ">>>"

print "Copying from %s to %s" % (from_file, to_file)

in_data = open(from_file).read() #short ver. of the above 2 lines

print "Does the output file exsist? %r" % exists(to_file)

out_file = open(to_file, 'w').write(in_data)

print "Alright, all done."
