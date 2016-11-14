# Enter your code here. Read input from STDIN. Print output to STDOUT
nStudent = int(raw_input().strip())
studentDict = dict()
desStudent = 'None'
for j in range(nStudent):
    arr = (raw_input().strip().split(' '))
    total = 0
    stName = arr[0]
    for i in range(len(arr)):
        if i !=0:
            total = total + float(arr[i]) 
    studentDict[stName] = total /(len(arr)-1.00)
    if(nStudent-1) == j:
        desStudent = stName
print "%.2f" % studentDict[desStudent]