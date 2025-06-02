#ANAGRAMS PROGRAM
a="silent"
b="listen"
if sorted(a)==sorted(b) and len(a)==len(b):
    print('ANAGRAMS')
else:
    print("NOT AN ANAGRAMS")

#using dictionary
a="listen"
b="silent"
f={}
f1={}
for i in a:
    if i not in f:
        f[i]=1
    else:
        f[i]+=1
for i in b:
    if i not in f1:
        f1[i]=1
    else:
        f1[i]+=1
if f==f1:
    print("ANAGRAMS")
else:
    print("NOT AN ANAGRAMS")
        
