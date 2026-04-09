def dfs(value, lst, depth, N):
    global cnt 
    # and dpeth를 하는 이유는 최소한 원소를 1개 이상 갖는 경우에만 정답으로 처리해주기 떄문입니다.
    if value == S and depth:
        cnt += 1

    for i in range(depth, N):
        value += lst[i]
        dfs(value, lst, i+1, N)
        value -= lst[i]
        

if __name__ == "__main__" :
    
    N, S = map(int, input().split())
    lst = list(map(int, input().split()))
    lst = sorted(lst)
    
    cnt = 0
    value = 0
    
    dfs(value, lst, 0, N )
    print(cnt)