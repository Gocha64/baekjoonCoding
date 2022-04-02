import math

def getPrime(n):
    primeFilter = [False, False] + [True] * (n-1)

    for i in range(2, n+1):
        if primeFilter[i]:
            for j in range(2*i, n+1, i):
                primeFilter[j] = False
    return primeFilter


primeList = getPrime(246912)

while(True):
    n = int(input())


    if n == 0:
        break

    count = 0
    for i in range(n+1,n * 2 + 1):
        if primeList[i]:
            count += 1
    print(count)
    
