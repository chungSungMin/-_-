def dfs(depth, value):
    global ans 
    if value == M and depth : 
        ans += 1

    for i in range(depth, N):
        value += lst[i]
        dfs(i+1, value)
        value -= lst[i]
            

if __name__ == "__main__" :
    N, M = map(int, input().split())
    lst = sorted(list(map(int, input().split())))
    value = 0
    ans = 0
    
    dfs(0, 0)
    print(ans)
