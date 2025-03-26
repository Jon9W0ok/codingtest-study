from collections import deque

def solution(name):
    def numberfy(name):
        return [ord(ch) - ord('A') for ch in name]

    target = numberfy(name)
    N = len(target)
    start = [0] * N

    queue = deque([(start, 0, 0)])
    visit = set()

    while queue:
        state, cursor, moves = queue.popleft()
        state_key = (tuple(state), cursor)
        if state_key in visit:
            continue
        visit.add(state_key)
        
        if state == target:
            return moves

        new_state = state.copy()
        new_state[cursor] = (new_state[cursor] + 1) % 26
        queue.append((new_state, cursor, moves + 1))

        new_state = state.copy()
        new_state[cursor] = (new_state[cursor] - 1) % 26
        queue.append((new_state, cursor, moves + 1))

        queue.append((state.copy(), (cursor + 1) % N, moves + 1))
        queue.append((state.copy(), (cursor - 1) % N, moves + 1))

print(solution("AAZ"))
