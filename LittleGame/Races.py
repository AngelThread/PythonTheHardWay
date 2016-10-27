class Races(object):
	name = "Base Race"
	
	
	def tellMeMyRace(self):
		print "Your race is %s" % Races.name

class HalfHuman(Races):
	name = "Half Human"

	def tellMeMyRace(self):
		print "Your race is %s" % HalfHuman.name