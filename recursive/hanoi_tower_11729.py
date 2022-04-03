def hanoi(_from, _by, _to,  n, moveList):
    if n == 1:
        moveList.append((_from, _to))

    else:
        hanoi(_from, _to, _by, n-1, moveList)
        moveList.append((_from, _to))
        hanoi(_by, _from, _to, n-1, moveList)



n = int(input())
moveList = []
hanoi(1, 2, 3, n, moveList)
print(len(moveList))
for i in moveList:
    print(f"{i[0]} {i[1]}")