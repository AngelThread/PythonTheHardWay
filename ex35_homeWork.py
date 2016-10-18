from sys import exit

questions = ["Which way do you want to go?","Right or Left?", "What is your age?"]

print "Shall we begin? "

userFirstAnswer = raw_input('> ')

def goForFun():
	print "Here you are for fun"


def startTheGame():
     
	 print "The game is started"
	 for i in range(0,2):
		print questions[i]



def  continueT():
	print "FFFFFF"


if userFirstAnswer.lower() == 'Yes'.lower():
	startTheGame()
	userDirectionAnswer = raw_input('> ')
	if userDirectionAnswer.lower() == 'right'.lower():
		print "You are hitting to the right"
	elif userDirectionAnswer.lower() == 'left'.lower():
		print "You are hitting to the left"
	else:
		print "You are in the nowhere man!"
else:
   
	exit(0)


