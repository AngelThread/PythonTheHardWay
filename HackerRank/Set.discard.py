n = int(raw_input())
setOf = set(map(int, raw_input().split())) 
#
for i in range(int(input())):  
    commandArr = list(raw_input().strip().split(' '))
   # print "len",len(commandArr)
    for k in range(len(commandArr)):     
        command = commandArr[k]
        #print "command", command
        try:
            if command == 'pop': 
                setOf.pop() 
                continue
            elif command == 'remove' and k+1 < len(commandArr):
                if commandArr[k+1].isdigit():
                    setOf.remove(int(commandArr[k+1]))
                    continue
                elif k+2 < len(commandArr) and commandArr[k+2].isdigit():
                    setOf.remove(int(commandArr[k+2]))
            elif command == 'discard'and k+1 < len(commandArr):
                if commandArr[k+1].isdigit():
                    setOf.discard(int(commandArr[k+1]))                    
                elif k+2 < len(commandArr) and commandArr[k+2].isdigit():
                    setOf.discard(int(commandArr[k+2]))
        except KeyError:
            continue

sumOfElements = 0
for y in setOf:
    sumOfElements = sumOfElements + int(y)
print sumOfElements