n = int(input())

row = [-1] * n

total = 0

#print(row)


def checkAttack(k):

    for i in range(k):
        if row[k] == row[i] or abs(k - i) == abs(row[k] - row[i]):
            return False

    return True




def dfs(k):

    global total

    if k == n:
        total += 1
       #print("return")
        return

    for i in range(n):
        row[k] = i
        if checkAttack(k):
            dfs(k+1)

dfs(0)
print(total)