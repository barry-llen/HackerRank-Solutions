#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    count=0
    ls=[]
    maxi=0
    while n>0:
        if n%2==1:
            count+=1
        else:
            if count!=0:
                if count>maxi:
                    maxi=count
                count=0
        n=n//2
    if count>maxi:
        maxi=count
    print(maxi)
