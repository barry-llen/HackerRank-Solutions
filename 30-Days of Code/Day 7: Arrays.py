#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    s=""
    for i in range(len(arr)-1,-1,-1):
        s+=str(arr[i])
        s+=" "
    print(s)

