n=int(input())
phonebook={}
for i in range(n):
    k=list(map(str,input().strip().split(" ")))
    phonebook[k[0]]=k[1]
while True:
    try:
        name=input()
    except EOFError:
        break
    if name in phonebook:
        print(f"{name}={phonebook[name]}")
    else:
        print("Not found")
