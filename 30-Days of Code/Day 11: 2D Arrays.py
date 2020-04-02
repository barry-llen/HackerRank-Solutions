#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr=[]
    ls=[]
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    for i in range(6):
        for j in range(6):
            sumi=0
            if i>0 and j>0 and i<5 and j<5:
                sumi+=arr[i][j]+arr[i-1][j-1]+arr[i-1][j]+arr[i-1][j+1]+arr[i+1][j-1]+arr[i+1][j]+arr[i+1][j+1]
                ls.append(sumi)


    print(max(ls))
