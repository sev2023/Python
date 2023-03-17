# https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators

def wrapper(f):   # this is 'decorator'
    def fun(l):   # this is 'wrapper'
        # complete the function
        l = map(lambda x:f"+91 { x[-10:-5:]} { x[-5::] }", l)
        return f(l)   # this could be just 'f(l)'
    return fun

  
@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 
  
  
# sample input:
# ['+9178954 62130', '+9198756 41230', '+9191959 69878']
# required output:
# ['+91 78954 62130', '+91 98756 41230', '+91 91959 69878']
