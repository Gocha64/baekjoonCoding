aNum = int(input())

aList = list(map(int,input().split()))

# 덧셈, 뺼셈, 곱셈, 나눗셈 순서
opCount = list(map(int,input().split()))


m = 1000000000
M = -1000000000

def cppDivide(a, b):

    result = abs(a)//abs(b)

    if bool(a < 0) ^ bool(b < 0):
        return -result

    return result



def calculate(n, result):
    global m, M, opCount

    if n == aNum:
        #print(f'result {result}')
        m = min(m, result)
        M = max(M, result)

    if opCount[0] > 0:
        opCount[0] -= 1
        #print("+", end = ' ')
        calculate(n+1, result + aList[n])
        opCount[0] += 1

    if opCount[1] > 0:
        opCount[1] -= 1
        #print("-", end=' ')
        calculate(n + 1, result - aList[n])
        opCount[1] += 1

    if opCount[2] > 0:
        opCount[2] -= 1
        #print("*", end=' ')
        calculate(n + 1, result * aList[n])
        opCount[2] += 1

    if opCount[3] > 0:
        opCount[3] -= 1
        #print("/", end=' ')
        calculate(n + 1, cppDivide(result, aList[n]))
        opCount[3] += 1


calculate(1, aList[0])
print(M)
print(m)
