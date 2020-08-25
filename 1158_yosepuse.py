from collections import deque
n, k = map(int, input().split())
# num = list(range(1, n+1))

# idx = k-1
# print('<', end="")
# while len(num) > 1:
#     print(num.pop(idx), end=", ")
#     idx += (k-1)
#     idx %= len(num)

# print(f'{num.pop(idx)}>')

result = ''
num = deque(range(1, n+1))
while len(num) > 0:
    num.rotate(-(k-1))
    result += f"{num.popleft()}, "

print(f"<{result.rstrip(', ')}>")
