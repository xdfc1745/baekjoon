from collections import deque

def deque_process(n):
    for i in range(1, n+1):
        deque.append(i)

    while len(deque) != 1:
        a = deque.popleft()
        deque.rotate(-1)

    print(deque.popleft())

def deque_rule(n):
    pow_val = 1
    while pow_val < n:
        pow_val *= 2
    
    return pow_val - 2 * (pow_val - n)

    
n = int(input())
print(deque_rule(n))
