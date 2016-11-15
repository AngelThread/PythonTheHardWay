from nose.tools import *
from ex49 import *



def test_peekMethod():
	word_list = [('direction','north'),('direction','south'),('direction','east')]
	peeked = peek(word_list)
	print peeked[0]
	print peeked[1]
	assert_equal(peeked, ('direction','north'))

def test_matchMethod():
	word_list = [('direction','north'),('direction','south'),('direction','east')]
	peeked = peek(word_list)
	word = match(word_list,'direction')
	assert_equal(word,('direction','north'))

def test_parse_verb():
	word_list = [('the','north'),('verb','go'),('error','the')]
	print parse_verb(word_list)
	print word_list

test_parse_verb()