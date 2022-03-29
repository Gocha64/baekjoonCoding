
triList = []
while(True):
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    triList.append(sorted([a,b,c]))

for i in triList:
    a, b, c = map(pow, i, [2]*len(i))
    if c == (a + b):
        print("right")

    else:
        print("wrong")