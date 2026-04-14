# 해당 문제의 핵심은 중복되는 수열은 안된다는것
def dfs(result):

    # 종료조건
    if len(result) == M and len(result): 
        print(*result)
        return
    prev = -1
    for i in range(N):
        if prev != lst[i]: 
            result.append(lst[i])
            prev = lst[i]
            dfs(result) 
            result.pop()

if __name__ == "__main__" :
    N, M = map(int, input().split())
    lst = sorted(list(map(int, input().split())))
    result = []
        
    dfs(result)

