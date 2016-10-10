from sys import argv # imports python modules. 

script, filename = argv # assign the values that are taken from terminal

txt = open (filename) #  open related file that is found by filename and path

print "Here's your file %r:" %filename # Here just name of the file printed.
print txt.read() # This is the place where file is read and be printed content of file 

txt.close()

print "File is closed"
#print "Type the filename again:" # the name of the file path is demanded again on here.

#file_again = raw_input("> ") # it just demand raw inout from user

#txt_again = open(file_again) # this line reads the file

#print txt_again.read()# this line print the file content again
