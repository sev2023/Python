#https://www.hackerrank.com/challenges/itertools-product/problem

s1 = input().split()
s2 = input().split()
print(*((int(i),int(j)) for i in s1 for j in s2))
