https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true

def minion_game(string):
    # your code goes here
    comb = [string[i:][:j] for i in range(len(string)) for j in range(1,len(string[i:])+1)]
    K = dict((i, comb.count(i)) for i in comb if i[0] in "AEIOU")
    S = dict((i, comb.count(i)) for i in comb if i[0] not in "AEIOU")
    if sum(K.values()) > sum(S.values()):
        print("Kevin", sum(K.values()))
    else:
        print("Stuart", sum(S.values()))
    
    
if __name__ == '__main__':
    s = input()
    minion_game(s)
