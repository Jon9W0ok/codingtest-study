import sys
input = sys.stdin.readline

N, C = map(int, input().split())
house = []

for _ in range(0, N):
    point = int(input())
    house.append(point)

house.sort()
term = (house[-1] - house[0]) // (C-1)

def parametric_search(left, right):
    global C, house

    mid = (right + left) // 2
    if right - left <= 1:
        return left

    current = house[0]
    count = 1
    # 공유기 설치 몇 대 할 수 있는지 체크
    for i in range(1, len(house)):
        if house[i] >= current + mid:
            count += 1
            current = house[i]
    # 공유기 설치 수가 목표 보다 크면 공유기 사이 거리 늘림
    if count >= C:
        left = mid
    # 공유기 설치 수가 목표 보다 작으면 공유기 사이 거리 줄임
    else:
        right = mid

    return parametric_search(left, right)


result = parametric_search(0, term+1)
print(result)