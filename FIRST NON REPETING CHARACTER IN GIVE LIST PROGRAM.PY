#USING COUNT FUNCTION

a=[1,2,1,3,2,4,5,6,7,8]
for i in a:
    if a.count(i)==1:
        print(i)
        break
    

#USING DICTIONARY

a=[1,2,1,3,2,4,5,6,7,8]
f={}
for i in a:
    if i not in f:
        f[i]=1
    else:
        f[i]+=1
for k,v in f.items():
    if v==1:
        print(k)
        break
   
