N = int(input())

b3 = 0
b5 = 0

b5 = N//5
N = N%5


if N == 1:
    b5 -= 1
    b3 += 2

elif N == 2:
    b5 -= 2
    b3 += 4

elif N == 3:
    b3 += 1

elif N == 4:
    b5 -= 1
    b3 += 3

if b5 < 0 or b3 < 0:
    print(-1)

else:
    print(b3+b5)
