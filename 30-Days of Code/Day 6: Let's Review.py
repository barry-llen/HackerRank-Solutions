n=int(input())
for i in range(n):
    s=""
    inp=input()
    for j in range(0,len(inp),2):
        s+=inp[j]
    s+=" "
    for j in range(1,len(inp),2):
        s+=inp[j]
    print(s)
