i = 0
numbers = []

#while i < 6:  
#	print "At the top i is %d" % i
#	numbers.append(i)

#	i = i + 1
#	print "Numbers now: ", numbers
#	print "At the bottom i is %d" % i

#print "The numbers:"



for num in numbers:
    print num

def insteadOfWhile (rangeLasts):    
	for i in range(0,rangeLasts):
	  
		print "At the top i is %d" % i
		numbers.append(i)
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
	
	print "The numbers"

insteadOfWhile(6)