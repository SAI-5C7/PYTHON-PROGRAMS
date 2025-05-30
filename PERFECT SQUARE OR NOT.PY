n=int(input("enter a number:"))
b=[i**2 for i in range(n+1)]
if n in b:
    print("perfect square")
else:
    print("not a perfect square")
