# problem: find all numbers which are less than number N and which have the digit d repeating exactly k times

# approach: digit dp. let's construct numbers which satisfies the constraints.

from functools import lru_cache

N,d,k = str(100),1,1

@lru_cache
def func(pos,count,valid):
    '''
        recursive function to solve the problem
        @param pos: (int) the position from left in the number that we construct
        @param count: (int) the number of times that digit d has repeated until pos
        @param valid: (bool) tells us whether there exists atleast one t such that 1<=t<pos and num[t]<b[t]

        @returns number of such numbers that saisfy the constriant
    '''
    
    # base case:
    if count>k:
        return 0
    
    # base case:
    if pos==len(N):
        return 1 if count == k else 0
    
    largest_possible_digit = 9 if valid else int(N[pos])
    
    # loop through all the 10 digits and try them all at pos
    ans = 0
    for i in range(largest_possible_digit+1):
        if not valid:
            # it means no digit prior was less than its corresponding position in N
            ans += func(pos+1, count+1 if i==d else count, i<int(N[pos]))
        else:
            # we have atleast one digit which is less than its corresponding position in N
            ans += func(pos+1,count+1 if i==d else count, valid)
        
    return ans

print(func(0,0,False))
