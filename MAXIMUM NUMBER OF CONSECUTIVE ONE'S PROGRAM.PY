a = [1,0,1,1,1,0,1,0]
m = 0
c = 0
for i in a:
    if i == 1:
        c += 1
        if c > m:
            m = c
    else:
        c = 0
print(m)
