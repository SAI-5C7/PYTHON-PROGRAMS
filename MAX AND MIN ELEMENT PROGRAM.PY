#MAX ELEMENT WITHOUT USING BUILT IN FUNCTION
a=[1,4,2,6,8,3,4,9]
m=0
for i in a:
    if i>m:
        m=i
print(m)   

#USING BUILT IN FUNCTION
a=[1,4,2,6,8,3,4,9]
print(max(a))

#MIN ELEMENT WITHOUT USING BUILT IN FUNCTION
a=[2,4,3,5,6,1,8,9]
b=a[0]
for i in a:
    if i<b:
        b=i
print(b)   

#USING BUILT IN FUNCTION
a=[2,4,3,5,6,1,8,9]
print(min(a))
