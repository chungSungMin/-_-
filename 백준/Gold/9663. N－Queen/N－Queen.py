def dfs(depth) : 
    global ans
    if depth == N : 
        ans +=1 
        return 

    else : 
        for i in range(N):
            if visited_col[i] == visited_dia_right[depth+i] == visited_dia_left[depth-i+(N-1)] == 0 : 
                visited_col[i] = visited_dia_left[depth-i+(N-1)] = visited_dia_right[depth+i] = 1
                dfs(depth+1)
                visited_col[i] = visited_dia_left[depth-i+(N-1)] = visited_dia_right[depth+i] = 0
    

if __name__ == "__main__" :
    N = int(input())
    ans = 0
    
    visited_col = [0 for _ in range(N)]
    visited_dia_right = [0 for _ in range(2*N-1)]
    visited_dia_left = [0 for _ in range(2*N-1)]
    
    dfs(0)
    print(ans)