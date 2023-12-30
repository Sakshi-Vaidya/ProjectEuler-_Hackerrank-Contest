import math
import os
import random
import re
import sys

def euler(n):
    sum = 0
    sum_squares = 0
    for x in range(1, n+1):
        sum += x
        sum_squares += x**2
    return sum**2-sum_squares

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        print(euler(n));