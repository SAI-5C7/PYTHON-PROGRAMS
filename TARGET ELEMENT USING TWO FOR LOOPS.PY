a=[1,2,3,4,5]
t=9
flag=False
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]+a[j]==t:
            print("TARGET FOUND AT INDEX:",i,j)
            flag=True
if(not flag):
    print("TARGET NOT FOUND")
