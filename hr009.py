#https://www.hackerrank.com/challenges/np-array-mathematics/problem

import numpy
numpy.set_printoptions(legacy='1.13')

N,M = map(int, input().split())
A = []
B = []

for _ in range(N):
    A.append(list(map(int, input().split())))
for _ in range(N):
    B.append(list(map(int, input().split())))

AA = numpy.array(A, int)
BB = numpy.array(B, int)

print(AA + BB)
print(AA - BB)
print(AA * BB)
print(AA // BB)
print(AA % BB)
print(AA ** BB)
