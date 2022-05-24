n, k = map(int, input().split())

a = []

for i in range(n):
    ai = int(input())
    if ai <= k:
        a.append(ai)


count = 0
while k != 0:
    for i in range(1, len(a)+1):
        distract = k - a[-1]
        if distract >= 0:
            k = distract
            count+=1
            break
        else:
            a.pop()
print(count)