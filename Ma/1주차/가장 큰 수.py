numbers = [1, 6, 1]

def dfs(numbers, visit, current):
    if sum(visit) == len(numbers):
        
        return current
    
    res = []
    
    for i in range(len(numbers)):
        if not visit[i]:
            visit[i] = 1
            res.append(dfs(numbers, visit, current + str(numbers[i])))
            visit[i] = 0
    
    return max(res, key=lambda x: int(x))

def solution(numbers):
    visit = [0] * len(numbers)
    return dfs(numbers, visit, "")

print(solution(numbers))
