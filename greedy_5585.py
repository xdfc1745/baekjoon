import sys
input = sys.stdin.readline

money = int(input())

change = 1000 - money
result = 0

# while change > 0:
#     if change >= 500:
#         result += 1
#         change -= 500
#     elif change >= 100:
#         result += 1
#         change -= 100
#     elif change >= 50:
#         result += 1
#         change -= 50
#     elif change >= 10:
#         result += 1
#         change -= 10
#     elif change > 5:
#         result += 1
#         change -= 5
#     elif change > 1:
#         result += 1
#         change -= 1

rest = [500, 100, 50, 10, 5, 1]

for i in rest:
    result += change // i
    change = change % i
    print(result, change)
print(result)
