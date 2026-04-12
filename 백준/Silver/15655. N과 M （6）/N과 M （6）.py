def dfs(depth):
    if len(result) == M :
        print(*result)
        return 
    else : 
        for i in range(depth, N):
            if visited[i] == 0 : 
                visited[i] = 1
                result.append(lst[i])
                dfs(i + 1)
                result.pop()
                visited[i] = 0


if __name__ == "__main__" :
    N, M = map(int, input().split())
    lst = sorted(list(map(int, input().split())))
    result = []
    visited = [0 for _ in range(N)]
    dfs(0)
