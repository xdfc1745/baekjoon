from collections import deque

n, m = map(int, input().split())
out = map(int, input().split()) # not list type

deque = deque([i for i in range(1, n+1)])
result = 0

for i in out:
    left = deque.index(i)
    right = len(deque) - left
    print(left, right)
    if left < right:
        result += left
        deque.rotate(-left)
        deque.popleft()
    else:
        result += right
        deque.rotate(right)
        deque.popleft()
    print(result)
    
print("result = ", result)