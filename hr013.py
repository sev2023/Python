# https://www.hackerrank.com/challenges/python-sort-sort/
# Sort subarrays based on their 'k' element (second element if k=1):

arr = [[10, 2, 5], [7, 1, 0], [9, 9, 9], [1, 23, 12], [6, 5, 9]]
k = 1

for i in sorted(arr, key=lambda x:x[k]):
        print(*i)
