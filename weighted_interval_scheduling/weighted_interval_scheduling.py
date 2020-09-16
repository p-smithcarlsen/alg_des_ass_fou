def opt(x: int) -> int:
    if x == 0:
        return intervals[0]
    elif x == 1:
        return intervals[1]
    else:
        max(opt(x-1), opt(x-2))

N = int(input())
intervals = []

for _ in range(N):
    next_interval = tuple(map(int, input().split()))
    intervals.append(next_interval)

intervals.sort(key = lambda intv: intv[1], reverse = True)
opt(N)