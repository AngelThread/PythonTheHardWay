# Enter your code here. import __builtin__Read input from STDIN. Print output to STDOUT
import __builtin__
#nCount =  [int(a) for a in raw_input().strip().split()] 
nData = raw_input()
list = map(int,raw_input().strip().split())
aTuple = tuple(list)
print hash(aTuple)