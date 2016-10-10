from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how?

in_file = open(from_file)
indata = in_file.read()
indata = indata + "\n"+"And I am the one to2"

print "The input file is %d bytes long" % len(indata)
print "Does the output file exists? %r"  % exists(to_file)
raw_input()

out_file = open(to_file,'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()





