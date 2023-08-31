# Always try to use 1-based index for segment tree.
# root node at index 1 will have information over the entire array

# segment tree for sum query
arr = [1,3,-5,6,8,9]
tree = [0]*len(arr)*4

def build(v,l,r):
    if l==r:
        tree[v] = arr[l]
        return
    mid = (l+r)//2
    build(2*v,l,mid)
    build(2*v+1,mid+1,r)
    tree[v] = tree[2*v]+tree[2*v+1]

def sum(v,l,r,ql,qr):
    '''
        v: current vertex
        l,r: boundary of current segments
        ql,qr: query range for which we want sum
    '''
    if ql>qr:
        return 0
    if ql==l and qr==r:
        return tree[v]
    mid = (l+r)//2
    if qr<=mid:
        return sum(2*v,l,mid,ql,qr)
    elif ql>mid:
        return sum(2*v+1,mid+1,r,ql,qr)
    else:
        return sum(2*v,l,mid,ql,mid)+sum(2*v+1,mid+1,r,mid+1,qr)

def update(v,l,r,pos,val):
    '''
        v: current vertex
        l,r: left and right boundary of current segment
        pos: update position
        val: new value
    '''
    if l==r:
        tree[v]=val
        return
    mid = (l+r)//2
    if pos<=l:
        update(2*v,l,mid,pos,val)
    else:
        update(2*v+1,mid+1,r,pos,val)
    tree[v] = tree[2*v]+tree[2*v+1]
    return

# segment tree for min in range query
arr = [1,3,-5,8,9]
tree = [float('inf')]*len(arr)*4
def build(v,l,r):
    '''
        v: current vertex
        l,r: left and right boundary of current segments
    '''
    if l==r:
        tree[v]=arr[l]
        return
    mid = (l+r)//2
    build(2*v,l,mid)
    build(2*v+1,mid+1,r)
    tree[v]=min(tree[2*v],tree[2*v+1])
    return

def find(v,l,r,ql,qr):
    '''
        finds minimm in the given range
    '''
    if ql>qr:
        return float('inf')
    if ql==l and qr==r:
        return tree[v]
    # check if belongs to left or right child
    mid = (l+r)//2
    if qr<=mid:
        return find(2*v,l,mid,ql,qr)
    elif ql>mid:
        return find(2*v+1,mid+1,r,ql,qr)
    else:
        return min(find(2*v,l,mid,ql,mid),find(2*v+1,mid+1,r,mid+1,qr))

def update(v,l,r,pos,val):
    '''
        updates the value at the given position and still retains the segment tree
    '''
    if l==r:
        tree[v] = val
        return
    mid = (l+r)//2
    if pos<=mid:
        update(2*v,l,mid,pos,val)
    else:
        update(2*v+1,mid+1,r,pos,val)
    tree[v] = min(tree[2*v],tree[2*v+1])

    
