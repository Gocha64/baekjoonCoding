n = int(input())

aList = list(map(int,input().split()))

# 덧셈, 뺼셈, 곱셈, 나눗셈 순서
opCount = list(map(int,input().split()))

opList = [-1] * (n-1)


m = 999999999999999999
M= -9999999999999999

def calculate():
    result = aList[0]
    for i in range(1, n-1):
        if opList[i] == 0:
            result += aList[i]
        elif opList[i] == 1:
            result -= aList[i]
        elif opList[i] == 2:
            result *= aList[i]
        elif opList[i] == 3:
            result //= aList[i]

"""
def dfs(k):
    if k == n-1:
        print(M)
        print(m)
        return

    for i in range(4):
        if opCount[i] > 0:
            opList[k] = i
            opCount[i] -= 1

"""