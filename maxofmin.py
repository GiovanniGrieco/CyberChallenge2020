#!/usr/bin/python3

from collections import deque

def solve(N, V):
    solution = deque()

    for ssize in range(1, N + 1):
        _max = max([
            min(V[i:i + ssize])
            for i in range(0, N + 1 - ssize)])
        
        solution.append(_max)

    return solution

if __name__ == '__main__':
    N = int(input().strip())
    V = list(map(int, input().strip().split(' ')))
    print(' '.join(map(str, solve(N, V))))

