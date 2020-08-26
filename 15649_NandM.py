def bfs(now, end, n, result, used):
    if  now >= end:
        print(' '.join(map(str, result)))
    else:
        for i in range(1, n+1):
            if not used[i]:
                used[i] = True
                bfs(now+1, end, n, result+[i], used)
                used[i] = False

n, m = map(int, input().split())
used_list = [False] * (n+1)
bfs(0, m, n, [], used_list)