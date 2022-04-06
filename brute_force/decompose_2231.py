n = int(input())


def getDecompose(n):
    sum = n

    for i in str(n):
        sum += int(i)

    return sum



i = 1
while(True):
    if i == n:
        print(0)
        break

    if n == getDecompose(i):
        print(i)
        break

    i += 1