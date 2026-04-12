def dfs(result):
    # 종료조건
    if len(result) == M : 
        print(*result)
        return
    else : 
        for i in range(N):
            result.append(lst[i])
            dfs(result) 
            result.pop()
    
    
if __name__ == "__main__" :
    N, M = map(int, input().split())
    lst = sorted(list(map(int, input().split())))
    result = []
        
    dfs(result)

