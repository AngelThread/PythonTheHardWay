
# Parts are defined
class Parts(object):
	parts = {
	'start':'You felt on a rough ground, you are standing up and looking at the long and seems endless hall',
	'second':'Everywhere is pink now! You are in a pink jungle', 
	'third':'Now You are in a island',
	'fourth':'You find yourself in a space ship'
	}
	
	partNumb = {
	1:'start',
	2:'second',
	3:'third',
	4:'fourth'
	}

	def __init__(self):
		pass


	def next_part(self,key):
		retValue = None
		for number, partId in self.partNumb.iteritems():
			if partId == key:
				if self.checkISValidKey(number+1):
					retValue = self.parts[self.partNumb[number+1]]
		return retValue

		
	def checkISValidKey(self,number):
		flag = False
		for a_key in self.partNumb.keys():
			if number == a_key:
				flag = True
		return flag

class AfterLife(object):
	
	def tellYourPath(self,destinyKey):
		print "Your decision was %d and you will face your destiny" % destinyKey