# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" %(arg1, arg2)

#ok, that *args is actually pointless, we can jus do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" %(arg1, arg2)

# this just takes one argument
def print_one(arg1):
    print "arg1: %r" %arg1

# this one takes no arguments

def print_non():
    print "I got hothin'."

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("Fisrt")
print_none()

