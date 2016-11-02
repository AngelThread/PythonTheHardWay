class Races(object):
	name = "Base"

	def pickArace(self, number):
		race = Races()
		if number == 1:
			return race
		elif number == 2:
			race = Ork()
			return race
		elif number == 3:
			race = HalfHuman()
			return race
		elif number == 4:
			race = ManKind()
			return race
		else: 
			return None
	
	def tellMeMyRace(self):
		print "You are a %s" % Races.name


class Ork(Races):
	name = "Ork"

	def tellMeMyRace(self):
		print "You are an %s" % Ork.name


class HalfHuman(Races):
	name = "Half Human and Half Ork"

	def tellMeMyRace(self):
		print "You are a %s" % HalfHuman.name

class ManKind(Races):
	name = "Human"

	def tellMeMyRace(self):
		print "You are a %s" % ManKind.name