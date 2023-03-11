# https://www.hackerrank.com/challenges/maximize-it/problem

M, K = input().split()
lis = []

for _ in range(int(M)):
    lis.append(list(map(int, input().split()[1:])))
    
# input end
# compute start

r = []
rr = []

def recurse(r,a): # recursive function to compute permutations
    for i in a[0]:
        r.append(i)
        if len(a)>1:
            recurse(r,a[1:])
        rr.append(list(r))   # collects permutations
        r.pop()

recurse(r, lis);
# rr collects non full size permutation too and needs filtering
ff = list(filter(lambda x:len(x) == len(lis), rr))

# now find the closest modulo
print(max(sum(map(lambda x:x**2, i))%int(K) for i in ff))
