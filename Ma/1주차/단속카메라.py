routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]

def solution(routes):
    answer = 0
    routes.sort(key=lambda x: (x[1], x[0]))
    cameras = [routes[0][1]]
    
    for start, end in routes[1:]:
        if start > cameras[-1]:
            cameras.append(end)

    answer = len(cameras)
    return answer

print(solution(routes))