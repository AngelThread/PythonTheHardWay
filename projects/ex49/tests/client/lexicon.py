class Lexicon(object):

	direction_words = ['north','south','east','west','down','up','left','right','back']
	verb_words = ['go','stop','kill','eat'] 
	stop_words = ['the','in','of']
	noun = ['bear','princess']

	def scan(self,input):
		words = input.split()
		retArray = []
		key = 'direction'
		print "Length ",len(words)
		retValeu = None
		for i in range(0,len(words)):
			retValeu = words[i]
			if words[i].lower() in self.direction_words:
				key = 'direction'
			elif words[i].lower() in self.verb_words:
				key = 'verb'
			elif words[i].lower() in self.stop_words:
				key = 'stop'
			elif words[i].lower() in self.noun:
				key = 'noun'
			else:
				retValeu = self.convert_number(words[i])
				if retValeu == None:
					retValeu = words[i]
					key = 'error'
				else:
					key = 'number'
			retArray.append((key,retValeu))
		return retArray

	def convert_number(self,input):
		try:
			return int(input)
		except ValueError:
			return None
