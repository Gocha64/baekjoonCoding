s = []

def dfs(n, m, depth):
    if m == depth:
        print(' '.join(map(str, s)))
        return

    for i in range(1, n+1):
        s.append(i)
        dfs(n, m, depth+1)
        s.pop()




n, m = map(int, input().split())
dfs(n, m, 0)
