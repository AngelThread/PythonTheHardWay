
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

print "Part Number :",partNumb[1]

for a_key in partNumb.keys():
	print a_key

for a_value in partNumb.values():
	print a_value
print "-----------------------------------------------------"
for number, partId in partNumb.iteritems():
	if number == 2:
		print partId
	else:
		print "Nope"

print "-----------------------------------------------------"

def checkISValidKey(number):
	flag = False
	for a_key in partNumb.keys():
		if number == a_key:
			flag = True
	return flag


print checkISValidKey(1)