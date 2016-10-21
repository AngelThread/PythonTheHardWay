class Song(object):

    
	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_day = Song (["Happy birthday to you", "I don't want to get sued","So I stop right there!"])

bulls_pn_parade = Song (["They rally around the family","With pockets full of shells"])

happy_day.sing_me_a_song()

bulls_pn_parade.sing_me_a_song()

