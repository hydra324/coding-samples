# let us frist define how a fenwick tree looks like
# its nothing but a array with non-linear jumping traversal
# we actually traverse the tree in a binary way by jumping between the bits

max_index = 100
bits = [0]*max_index

def update(idx):
    while idx < max_index:
        bits[idx] += 1
        idx += idx & -idx
        
def get_sum(idx):
    ans = 0
    while idx>=1:
        ans += bits[idx]
        idx -= idx & -idx
    return ans
