n=int(input("enter a number:"))
l=0
r=n
flag=False
while(l<=r):
    mid=(l+r)//2
    s=mid*mid
    if s==n:
        print("square root of given number is:",mid)
        flag=True
        break
    elif s<n:
        l=mid+1
    else:
        r=mid-1
if(not flag):
    print("not possible to find exact square root")
    
