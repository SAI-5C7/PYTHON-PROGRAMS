(1)FIBONACCI SEQUENCE USING FUNCTIONS

def pavan(n): #where n is size of fibonacci sequence
    a,b=0,1
    print(a,b,end=" ")
    for i in range(2,n):
        c=a+b
        print(c,end=" ")
        a,b=b,c
pavan(6)



(2)FIBONACCI SEQUENCE USING BOTTOM UP(TABULATION) METHOD

def sai(n):
    l=[0,1]
    for i in range(2,n):
        l.append(l[i-1]+l[i-2])
    print(*l)
sai(6)


(3)FIBONACCI SEQUENCE USING TOP-DOWM(MEMOTIZATION) METHOD

def nani(n, memo=None):
    if memo is None:
        memo = {}
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = nani(n-1, memo) + nani(n-2, memo)
    return memo[n]
print(nani(5)) 
