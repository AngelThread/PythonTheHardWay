# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input().strip())
arr = raw_input().strip().split()
bigBoy = -100
med = -100
smallest = -100
for i in xrange(n):
    i = int(arr[i])
    if i > bigBoy :
        bigBoy = i

for i in xrange(n):
    i = int(arr[i])
    if (i > med) and ( i < bigBoy) :
        med = i
        
print med
    
