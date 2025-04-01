import sys
input = sys.stdin.readline

N, M, x, y, r = map(int, input().split())

maps = []
for row in range(N):
    maps.append(list(map(int, input().split())))

direction = list(map(int, input().split()))

bottom = 6
top = 7 - bottom
dice = [6, 3, 4, 5, 2]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
scores = [0] * 6

for d in direction:
    # 1.이동 
    x += dx[d-1]
    y += dy[d-1]
    if x < 0 or x >= M:
        x -= dx[d-1]
        continue
    if y < 0 or y >= N:
        y -= dy[d-1]
        continue

    #2. 주사위 밑면 확인
    nd = ((d-1) ^ 1) + 1
    
    dice[0], dice[nd] = dice[d], dice[0]
    dice[d], top = top, 7-dice[0]

    #3. 지도 <-> 주사위 밑면
    if not maps[y][x]:
        maps[y][x] = scores[dice[0]-1]
    else:
        scores[dice[0]-1], maps[y][x] = maps[y][x], 0

    #4. 출력
    print(scores[top-1])
    # print(maps)
    # print()
   