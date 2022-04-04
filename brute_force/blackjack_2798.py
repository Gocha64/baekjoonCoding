n, m = map(int,input().split())
cards = list(map(int,input().split()))
cards.sort()

max = 0

for i in range(0, n):
    sum = cards[i]
    if sum > m:
        break

    for j in range(i + 1, n):
        sum = cards[i] + cards[j]
        if sum > m:
            break

        for k in range(j + 1, n):
            sum = cards[i] + cards[j] + cards[k]
            #print(cards[i], cards[j], cards[k], sum)
            if sum > m:
                break
            if max < sum:
                max = sum

print(max)
