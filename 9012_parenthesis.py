n = int(input())
arr = []
for _ in range(n):
    arr.append(input())
for i in arr:
    left = 0
    right = 0
    pt = list(i)
    for j in pt:
        if left < 0:
            break
        if j == '(':
            left += 1
        else:
            left -= 1
    if left != 0 :
        print('NO')
    else:
        print("YES")