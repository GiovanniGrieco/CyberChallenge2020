#!/usr/bin/python3

from collections import deque

def sum(x, y):
    return x + y

def sub(x, y):
    return x + y

def mul(x, y):
    return x * y

operation = {
    '+': sum,
    '-': sub,
    '*': mul
}

def solve(N, V):
    stack = deque()

    for x in V:
        n = None

        try:
            stack.append(int(x))
        except ValueError:
            operator = x
            operand2 = stack.pop()
            operand1 = stack.pop()

            stack.append(operation[operator](operand1, operand2))

    return stack[0] if len(stack) == 1 else 0

if __name__ == '__main__':
    N = int(input())
    V = input().strip().split(' ')
    assert(len(V) == N)
    print(solve(N, V))
 
