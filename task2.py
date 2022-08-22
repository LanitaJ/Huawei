# Task 2. Greatest Number

def find(l, r, num, s):
    while (l < r):
        mid = (l + r) // 2
        if (s[mid] <= num):
            l = mid + 1
        else:
            r = mid
    return l - 1

case_num = 1
while (True):
    s = []
    n, m = [int(x) for x in input().split()]
    if n == m == 0:
        break
    a = [int(input()) for _ in range(n)] + [0]
    k = 0
    for i in a:
        for j in a:
            if (i + j <= m):
                s.append(i + j)
    s.sort()
    result = 0
    for si in s:
        m_ = m - si
        x = find(0, len(s), m_, s)
        result = max(result, si + s[x])
    print(f"Case {case_num}: {result}\n")
    case_num += 1
