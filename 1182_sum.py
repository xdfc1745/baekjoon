# 5 0
# -7 -3 -2 5 8

def make_subseq(now_idx, total_sum, s, num_list):
    if now_idx >= len(num_list):
        if total_sum == s:
            return 1
        return 0
    else:
        used_cnt = make_subseq(now_idx+1, total_sum +
                               num_list[now_idx], s, num_list)
        unused_cnt = make_subseq(now_idx+1, total_sum, s, num_list)
        return used_cnt + unused_cnt


n, s = map(int, input().split())
num_list = list(map(int, input().split()))

result = make_subseq(0, 0, s, num_list)

if s == 0:
    result -= 1
print(result)
