#!/usr/bin/python3

def solve(N, K, V):
    solution = 0

    for x in range(len(V)):
        s = sum([
            -V[i] * (2 ** i)
            for i in range(len(V))
            if i != x])

        if s % (2 ** x) == 0:
            s = s / (2 ** x)
        if abs(s) <= K:
            solution += 1

    return solution

if __name__ == '__main__':
    N, K = map(int, input().strip().split(' '))
    V = list(map(int, input().strip().split(' ')))
    print(solve(N, K, V))

