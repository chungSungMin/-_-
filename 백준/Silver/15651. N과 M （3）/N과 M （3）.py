def dfs(depth):
    if len(lst) == M :
        print(*lst)
        return 
    else : 
        for i in range(depth, N):
            lst.append(i+1)
            dfs(depth)
            lst.pop()


if __name__ == "__main__" :
    N, M = map(int, input().split())
    lst = []
    visited = [0 for _ in range(M)]

    dfs(0)
