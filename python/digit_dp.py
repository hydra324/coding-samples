# problem: find all numbers which are less than number N and which have the digit d repeating exactly k times

# approach: digit dp. let's construct numbers which satisfies the constraints.

from functools import lru_cache

N,d,k = str(10**10),5,3
size = len(N)

@lru_cache
def func(pos,count,valid):
    '''
        recursive function to solve the problem
        @param pos: (int) the position from left in the number that we construct
        @param count: (int) the number of times that digit d has repeated until pos
        @param valid: (bool) tells us whether for all positions t such that 1<=t<pos, num[t]<b[t]

        @returns number of such numbers that saisfy the constriant
    '''

    # # base case:
    # if not valid:
    #     return 0
    
    # base case:
    if count>k:
        return 0
    
    # base case:
    if pos==size:
        return 1 if count == k else 0
    
    # loop through all the 10 digits and try them all at pos
    ans = 0
    for i in range(10 if valid else int(N[pos])):
        ans += func(pos+1, count+1 if i==d else count, valid and i<int(N[pos]) if not valid else i<int(N[pos]))
    return ans

print(func(0,0,True))
        
