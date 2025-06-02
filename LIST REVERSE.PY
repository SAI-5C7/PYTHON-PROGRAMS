#LIST REVERSE 
a=[3,2,5,4,6,8,1,9]
b=[]
for i in range(len(a)-1,-1,-1):
    b.append(a[i])
print(b) 


#USING REVERSE BUILT IN FUNCTION
a=[3,2,5,4,6,8,1,9]
a.reverse()
print(a)
    
