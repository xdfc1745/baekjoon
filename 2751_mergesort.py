def merge(num):
    if len(num) < 2:
        return num

    mid = len(num) // 2
    l_arr = merge(num[:mid])
    r_arr = merge(num[mid:])

    merged_arr = []
    l = h = 0
    while l < len(l_arr) and h < len(r_arr):
        if l_arr[l] < r_arr[h]:
            merged_arr.append(l_arr[l])
            l += 1
        else:
            merged_arr.append(r_arr[h])
            h += 1
    merged_arr += l_arr[l:]
    merged_arr += r_arr[h:]
    return merged_arr

n = int(input())

num = []
for _ in range(n):
    num.append(int(input()))

print(merge(num))