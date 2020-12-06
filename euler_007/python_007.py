#!/bin/python3

import sys
import math

t = int(input().strip())
def gen_primes(maxPrime:int):
    """ Generates a list of the Primes up to the argument given """
    def genSetNum(num, maxPrime):
        return set(range(num*2,maxPrime+1,num))

    allSet = genSetNum(1,maxPrime) - genSetNum(2,maxPrime)
    for i in range(3,math.ceil(math.sqrt(maxPrime)),2):
        if i in allSet:
            tempSet = genSetNum(i, maxPrime)
            allSet = allSet - tempSet
    return(sorted(list(allSet)))

primes_list = gen_primes(10**6)

for a0 in range(t):
    n = int(input().strip())
    print(primes_list[n-1])