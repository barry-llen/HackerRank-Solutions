# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
n=int(input())
for _ in range(n):
    num=int(input())
    flag=0
    if num==0 :
        print("Not prime")
        continue
    if num==1:
        print("Not prime")
        continue
    if num==2:
        print("Prime")
        continue
    if num>2 and num%2==0:
        print("Not prime")
        continue
    for i in range(3,math.floor(math.sqrt(num))+1,2):
        if num%i==0:
            flag=1
            break
    if flag==1:
        print("Not prime")
    else:
        print("Prime")


