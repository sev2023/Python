# https://www.hackerrank.com/challenges/py-set-discard-remove-pop

n = int(input())
s = set(map(int, input().split()))

for _ in range(int(input())):
    op_name, *op_args = input().split()
    
    # * * * * * getattr() * * * * * 
    #    example:
    #
    #    a = "abc"
    #    b = getattr(a, "upper")
    #    "b()" will behave same as "a.upper()" 
    #
    set_op = getattr(s, op_name)

    set_op(*[int(x) for x in op_args])

print(sum(s))
