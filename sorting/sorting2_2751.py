#pypy3로 채점

n = int(input())

l = []
for i in range(n):
    l.append(int(input()))

for i in sorted(l):
    print(i)