# https://www.hackerrank.com/challenges/exceptions/problem

for _ in range(int(input())):
    a,b = input().split()
    try:
        print(int(a) / int(b))
    except Exception e:
        print(e)
