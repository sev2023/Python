#https://www.hackerrank.com/challenges/iterables-and-iterators/problem
#no need itertoold to solve this
l,s,t = int(input()), input().split(), int(input())  
r = 0  
for i in range(t):  
  if (l - s.count("a")) < t:r = 1  
  r = r + (1 - r) * s.count("a") / (l - i)  
print(r) 
