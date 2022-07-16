n = int(input())
m = []

for i in range(n):
    m.append(tuple(map(int, input().split())))



m.sort(key =  lambda x : (x[1], x[0]))

count = 1
end = m[0][1]

for i in range(1, n):
    if end <= m[i][0]:
        end = m[i][1]
        count += 1

print(count)