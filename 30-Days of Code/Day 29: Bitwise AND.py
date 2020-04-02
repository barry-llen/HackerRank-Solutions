#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])
        maxi=0
        if k|(k-1)<=n:
            maxi=k-1
        else:
            maxi=k-2
        print(maxi)
