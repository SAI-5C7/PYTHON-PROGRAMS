(1)

a = "a100b200c300"
i = 0
output = ""
while i < len(a):
    char = a[i]
    i += 1
    num = ""
    while i < len(a) and a[i].isdigit():
        num += a[i]
        i += 1
    output +=char * int(num)
print(output)





(2)

a="a3b4c5"
for i in range(0,len(a),2):
    print(a[i]*int(a[i+1]),end="")
