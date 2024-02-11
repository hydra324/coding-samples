S = 'ABC ABCDAB ABCDABCDABDEABCDABD' # main string
W = 'ABCDABD' # pattern

# first we gotta build the lookup table
# which tells us the longest prefix which is also a suffix ending at every index in the table
lps = [0]*len(W) # longest prefix-suffix
prev_lps,i = 0,1 # start from 1, because we already know that lps at index 0 is 0
while i<len(W):
    if W[i]==W[prev_lps]:
        lps[i],prev_lps=prev_lps+1,prev_lps+1
        i+=1
    elif prev_lps==0:
        lps[i]=0
        i+=1
    else:
        prev_lps = lps[prev_lps-1]
print('lps:',lps)

ans = []

# now that we have the lookup table, we can start searching for the pattern in the main string
i,j = 0,0 # ptr for main string, ptr for pattern
while i<len(S):
    if S[i]==W[j]:
        i,j = i+1,j+1
    else:
        if j==0:
            i += 1
        else:
            j = lps[j-1]
    if j==len(W):
        ans.append(i-len(W))
        j = lps[j-1]
print('ans:',ans)
for a in ans:
    print(f'found pattern starting at index {a} : {S[a:a+len(W)]}')