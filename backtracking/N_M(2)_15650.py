s = []

def dfs(n, m, depth = 0, k = 0):
    for i in range(depth+1, n+1):
        if (i not in s) and (i > k):
            s.append(i)
            dfs(n, m, depth+1, i)
            s.pop()



    if depth == m:
        print(' '.join(map(str,s)))



n, m = map(int, input().split())
dfs(n,m)