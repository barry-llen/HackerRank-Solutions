#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    dic={}
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        x=re.search("@gmail.com",emailID)
        if x:
            dic[emailID]=firstName
    sort_arr=sorted(dic.items(),key=lambda x:x[1])
    for i in sort_arr:
        print(i[1])
    
