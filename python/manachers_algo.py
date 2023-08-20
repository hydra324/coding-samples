# manacher's algorithm is used to find all palindromic
# substrings in a given string in O(N) time
# afaik, this is the fastest algo to do so.

# approach: for each position we will find the number of palindromes
# centered at this position

# algo discovered by Glenn K. Manacher in 1975

# convert string into given format
s_dash = 'somestringcontainingpalindrome'
s = '#'+'#'.join(s_dash)+'#'
center=radius=0
radii = [0]*len(s)

for i in range(len(s)):
    mirror = 2*center - i

    # check if current index falls within the previous largest palindrome
    if i<radius:
        # if it is then, we bootstrap the radius at this index with the mirror's radius
        radii[i] = min(radius-i,radii[mirror])
    # expand on left and right to see if we can increase the radius
    while i-1-radii[i] >= 0 and i+1+radii[i] < len(s) and s[i-1-radii[i]]==s[i+1+radii[i]]:
        radii[i] += 1
    
    # check if the palindrome with centre at current radius is more than the previous
    # largest palindrome
    if i+radii[i] > radius:
        # update centre and radius
        center = i
        radius = i+radii[i]

# find largest among all palindromes
max_len = max(radii)
center_idx = radii.index(max_len)
start_idx = (center_idx - max_len)//2
palindrome = s_dash[start_idx:start_idx+max_len]
