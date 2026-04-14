# 해당 문제의 핵심은 중복되는 수열은 안된다는것
def dfs(depth, result):

    # 종료조건
    if len(result) == M and len(result): 
        print(*result)
        return
    prev = -1 # 중복수열 제거
    for i in range(depth, N):
        if prev != lst[i]: 
            result.append(lst[i])
            prev = lst[i]
            dfs(i, result)  # 비내림차순 설정 i
            result.pop()

if __name__ == "__main__" :
    N, M = map(int, input().split())
    lst = sorted(list(map(int, input().split())))
    result = []
        
    dfs(0, result)

