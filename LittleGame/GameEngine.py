from Parts import Parts
from Parts import AfterLife
from Races import Races
from Races import HalfHuman
from Races import ManKind

print " the part %s" % Parts.parts['start']
my = Parts()

print  "You have to draw your path yourself!"
#luckyNumber = int(raw_input("Tell me your lucky number")) #int method is used for convertion from String to int

luckyNumber = input("Tell me your lucky number: ") # raw_input doesn't evaluate the data and returns as it is, in string form. 

#But, input will evaluate whatever you entered and the result of evaluation will be returned 
try:
	if Parts.partNumb[luckyNumber] != None:
		print Parts.parts[Parts.partNumb[luckyNumber]]
		selection = Races()
		selection = selection.pickArace(luckyNumber) 
		selection.tellMeMyRace()
except KeyError, e:
	print "I've got key error!"