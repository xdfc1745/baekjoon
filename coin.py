# 첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 1 ≤ K ≤ 100, 000, 000)
# 둘째 줄부터 N개의 줄에 동전의 가치 A_i가 오름차순으로 주어진다.
# (1 ≤ A_i ≤ 1, 000, 000, A_1=1, i ≥ 2인 경우에 A_i는 A_(i-1)의 배수)
# 첫째 줄에 K원을 만드는데 필요한 동전 개수의 최솟값을 출력한다.

n, p = input().split()
num = int(n)
price = int(p)

money = []
for i in range(num):
    money.append(int(input()))

money = money[::-1]
# print(money)

cnt = 0
for i in money:
    cnt += price // i
    price = price % i
    if (price <= 0):
        break

print(cnt)
