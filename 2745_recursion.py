in_num, m = input().split()
n = int(m)
num = list(in_num)

# def numeral(num, n, cnt):
#     if cnt == len(num):
#         return 0
#     if num[cnt].isdigit():
#         return num[cnt] * (n**cnt) + numeral(num, n, cnt+1)
#     else:
#         temp = ord(num[cnt].upper())-ord('A') + 10
#         return temp * (n ** cnt) + numeral(num, n, cnt+1)


def numeral(num, n):
    result = 0
    l = len(num)-1
    for i in range(len(num)):
        if num[i].isdigit():
            print(num[i], n**(l-i))
            result += int(num[i]) * (n**(l-i))
        else:
            temp = ord(num[i].upper())-ord('A') + 10
            print(temp, n**(l-i))
            result += temp * (n**(l-i))
    return result

result = numeral(num, n)
print(result)