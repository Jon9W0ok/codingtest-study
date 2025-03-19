import sys
input = sys.stdin.readline

k = 80
dungeons = [[80,20], [50,40],[30,10]]

def dfs(k, dungeons, visit, ans=0):
    for i in range(len(dungeons)):
        mini, exh = dungeons[i]
        if k >= mini and not visit[i]:
            visit[i] = 1
            ans = max(dfs(k-exh, dungeons, visit, ans), sum(visit))
            visit[i] = 0
    return ans
    
def solution(k, dungeons):
    visit = [0] * len(dungeons)
    answer = dfs(k, dungeons, visit)
            
    return answer

print(solution(k, dungeons))
