#from nose.tools import *
import ex49

from lexicon import Lexicon


def test_directions():
	#word_list = ['a','b','c']
	lexicon = Lexicon()
	word_list = lexicon.scan("north")
	print word_list
	peeked = ex49.peek(word_list)
	print "Peek" ,peeked
	#assert_equal(peeked, 'a')
	#result = lexicon.scan("north south east")
	#assert_equal(result,[('direction','north'),('direction','south'),('direction','east')])
print "------------------------"

test_directions()