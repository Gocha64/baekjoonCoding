def dfs(depth, n, m, arr):


    for i in range(1, n + 1):
        #print(depth, n, m, arr)
        if i not in arr:
            arr.append(i)
            dfs(depth + 1, n, m, arr)
            arr.pop()

    if depth == m:
        print(' '.join(map(str,arr)))
        return



n, m = map(int, input().split())

arr = []
#print(n,m)




dfs(0, n, m, arr)