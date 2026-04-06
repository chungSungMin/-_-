

def dfs(n, lst): 
    if n == M :
        ans.append(lst)
        return 
    
    else : 
        for i in range(1, N+1) :
            if visited[i] == 0 : 
                visited[i] = 1
                dfs(n+1, lst + [i])
                visited[i] = 0
            else : 
                continue
        
    


if __name__ == '__main__' : 
    N, M = map(int, input().split())
    
    visited = [ 0 for _ in range(N+1)]
    
    ans = []
    dfs(0, [])
    
    for lst in ans : 
        print(*lst)
    