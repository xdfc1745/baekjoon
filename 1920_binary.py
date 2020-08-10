n = int(input())
a_list = map(int, input().split())
m = int(input())
x_list = map(int, input().split())

a_list = sorted(list(a_list))

for x in x_list:
    flag = 0
    start = 0
    end = len(a_list)-1
    while True:
        middle = start + ((end - start) // 2)
        if a_list[middle] == x:
            flag = 1
            break
        elif a_list[middle] < x:
            start = middle + 1
        elif a_list[middle] > x :
            end = middle - 1
        if len(a_list) <= start or start > end or len(a_list) <= end:
            break
    print(flag)
