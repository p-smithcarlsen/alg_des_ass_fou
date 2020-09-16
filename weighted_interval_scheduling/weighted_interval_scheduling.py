def opt(x: int):
    if W[x] != -1:
        res = W[x]
    

    if x == 0:
        res = intervals[0][2]
    elif x == 1:
        res = intervals[1][2]
    else:
        take = intervals[x][2] + intervals[x-2][2]
        drop = intervals[x-1][2]
        res = max(take, drop)
    return res

N = int(input())
intervals = [None] * N
W = [-1] * N

for i in range(N):
    next_interval = tuple(map(int, input().split()))
    intervals[i] = next_interval

intervals.sort(key=lambda intv: intv[1])
print(opt(N-1))
