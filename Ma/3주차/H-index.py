import sys
input = sys.stdin.readline

citations = [3, 0, 6, 1, 5]

def solution(citations):
    citations.sort() # 1. 정렬
    
    # 2. 
    n = len(citations)
    answer = n

    for i in range(n+1):
        num = 0
        for cite in citations:
            if i <= cite:
                num += 1

        if num < i:
            answer = i-1
            break    
    
    return answer

print(solution(citations))