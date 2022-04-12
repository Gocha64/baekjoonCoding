import sys

n = int(input())
count = [0 for i in range(10001)]

for i in range(n):
    a = int(sys.stdin.readline())
    count[a] += 1

#print("numLi\n",numList,sep='')
#print("count\n",count,sep='')

for i in range(len(count)):
    for j in range(count[i]):
        print(i)