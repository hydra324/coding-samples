# approach: for each position we will find the number of palindromes
# centered at this position

s = 'somestringwithpalindromes'
s_dash = '#' + '#'.join(s) + '#'
n = len(s_dash)
palindrome_radii = [0]*n
center = radius = 0

for i in range(n):
    mirror = 2*center -i
    if i<radius:
        palindrome_radii[i] = min(radius-i,palindrome_radii[mirror])
    while i+1+palindrome_radii[i] < n and i-1-palindrome_radii[i] >= 0 and s_dash[i+1+palindrome_radii[i]]==s_dash[i-1-palindrome_radii[i]]:
        palindrome_radii[i] += 1
    if i+palindrome_radii[i] > radius:
        center  = i
        radius = i+palindrome_radii[i]

max_len = max(palindrome_radii)
center_idx = palindrome_radii.index(max_len)
start_idx = (center_idx - max_len) // 2
longest_palindrome = s[start_idx:start_idx+max_len]