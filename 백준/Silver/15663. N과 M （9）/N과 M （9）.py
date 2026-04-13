# 해당 문제의 핵심은 중복되는 수열은 안된다는것
def dfs(result):

    # 종료조건
    if len(result) == M and len(result): 
        print(*result)
        return
    # 리스트를 sorting 할거기 떄문에 이전 element와 같다면 중복된 수열이 완성되므로 이전 값과 다른 경우에만 선택하도록 유도한다.
    prev = 0
    for i in range(N):
        if visited[i] == 0 and prev != lst[i]:
            result.append(lst[i])
            visited[i] = 1
            prev = lst[i]
            dfs(result) 
            result.pop()
            visited[i] = 0


if __name__ == "__main__" :
    N, M = map(int, input().split())
    lst = sorted(list(map(int, input().split())))
    visited = [0 for _ in range(N)]
    result = []
        
    dfs(result)

