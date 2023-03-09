# https://www.hackerrank.com/challenges/piling-up/leaderboard

for _ in range(int(input())):
    input()
    l = 0
    r = "Yes"
    a = list(map(int, input().split()))
    while a:
        if l > 0 and max(a[0],a[-1]) > l:
            r = "No"
            break
        if a[0] > a[-1]:
            l = a.pop(0)
        else:
            l = a.pop()
    print(r)
