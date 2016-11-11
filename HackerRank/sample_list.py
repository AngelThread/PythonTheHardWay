# Enter your code here. Read input from STDIN. Print output to STDOUT
list = []

n = int(raw_input('').strip())

for i in range(n):
	count = 0 
	#nCount = list.append(str(raw_input('').split(' ')))
	nCount =  [str(a) for a in raw_input().strip().split()] 
	keyVal = None
	firstArg= None
	secondArg = None
	for i in range(len(nCount)):
		if i == 0:
			keyVal = nCount[0]
		elif i==1:
			firstArg = nCount[1] 
		elif i == 2:
			secondArg = nCount[2] 
	if secondArg != None:
		getattr(list, keyVal)(int(firstArg.strip()), int(secondArg.strip()))
	elif firstArg != None: 
		getattr(list, keyVal)(int(firstArg.strip()))
	elif keyVal == 'print':
		print list
	else:
		getattr(list, keyVal)()

           