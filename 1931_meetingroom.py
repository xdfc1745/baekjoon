# 스케쥴링 문제는 끝부분이 가장 먼저 끝나는것부터 본다

n = int(input())

time_list = []
for _ in range(n):
    time_list.append(map(int, input().split()))
    # time = [s, e]
    # time_list.append(time)

time_list.sort(key=lambda row: [row[1], row[0]])

result = 1
end_time = time_list[0][1]

for i in range(1, len(time_list)):
    if time_list[1][0] >= end_time:
        end_time = time_list[i][1]
        result += 1

print(result)
