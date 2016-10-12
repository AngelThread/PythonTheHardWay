print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.' # look out for escape character '\'

# Three quotation mark does its job multi string
poem = """ 
\tThe lovely world 
with logic so firmly planted 
cannot discern \n the needs of lovely
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "----------"
print poem
print "----------"

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

# A method can return multiple things all at once
def secret_formula (started):
    
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars /100
	return jelly_beans, jars, crates

start_point = 10000
# A method multiple retruns assign in a single line as the bellow
beans, jars, crates = secret_formula(start_point)

print "With a starting point of :%d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10 

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)
