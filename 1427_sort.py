def quick_sort(num):
    if len(num) <= 1:
        return num
    pivot = num[0]

    less = []
    more = []
    same = []
    for n in num:
        if n < pivot:
            less.append(n)
        elif n > pivot:
            more.append(n)
        else:
            same.append(n)
    return quick_sort(less) + same + quick_sort(more)

num = input()
# num = []
# while n > 1:
#     num.append(int(n) % 10)
#     n /= 10

num_s = quick_sort(num)

cnt = 1
result = 0

for n in num_s:
    result += int(n) * cnt
    cnt *= 10

print(int(result))