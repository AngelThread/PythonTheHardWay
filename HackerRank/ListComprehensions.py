# Enter your code here. Read input from STDIN. Print output to STDOUT
x = int(raw_input().strip())
y = int(raw_input().strip())
z = int(raw_input().strip())
n = int(raw_input().strip())

b =0 
c =0
ListOfNumbers = [[a , b , c ]for a in range(x+1)  if a + b + c != n] # List of integers from
# for b in range(y) for c in range(z)
bOfNumbers = [[a , b , c ]for b in range(y+1)  if a + b + c != n] # List of integers from

cOfNumbers = [[a , b , c ]for c in range(z+1)  if a + b + c != n] # List of integers from

ListOfNumbers.append(bOfNumbers)
ListOfNumbers.append(cOfNumbers)
ListOfNumbers.sort()

print ListOfNumbers