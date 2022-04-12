n = int(input())

l = []
for i in range(n):
    l.append(int(input()))


# 버블
for i in range(n):
    for j in range(i, n):
        if l[i] > l[j]:
            temp = l[i]
            l[i] = l[j]
            l[j] = temp



for i in l:
    print(i)

