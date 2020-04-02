#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
totalcount=0
for i in range(n):
    count=0
    for j in range(0,n-1-i):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
            count+=1
    totalcount+=count
    if count==0:
        break
print(f"Array is sorted in {totalcount} swaps.")
print(f"First Element: {a[0]}")
print(f"Last Element: {a[n-1]}")

