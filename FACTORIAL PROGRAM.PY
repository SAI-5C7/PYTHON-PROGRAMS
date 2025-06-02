#USIMG MATH FUNCTION
import math
n=int(input("eneter a number:"))
print(math.factorial(n))

#ANOTHER METHOD
n=int(input("enter a number:"))
f=1
for i in range(1,n+1):
    f*=i
print(f)    
