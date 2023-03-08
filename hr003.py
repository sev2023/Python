# https://www.hackerrank.com/challenges/iterables-and-iterators/problem

input()
s = input().split()
t = int(input())



l = len(s)
r = 0;

for i in range(t):
    
    r = r + (1 - r) * (1 - (s.count('a')-i) / (l-i))
print(r)
