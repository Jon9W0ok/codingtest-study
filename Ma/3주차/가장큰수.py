import sys
input = sys.stdin.readline

numbers = [6, 10, 2]

def solution(numbers):
    answer = ''
    for num in numbers:
        answer += str(num)
    # answer = ''
    return answer

print(solution(numbers))