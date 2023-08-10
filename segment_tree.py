# segment tree for sum query
arr = [1,3,-5,6,8,9]
tree = [0]*len(arr)*4

def build(v,l,r):
    if l==r:
        tree[v] = arr[l]
        return
    mid = (l+r)//2
    return build(2*v,l,mid)+build(2*v+1,mid+1,r)

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
    return sum(2*v,l,mid,ql,min(mid,qr))+sum(2*v+1,mid+1,r,max(mid+1,ql),qr)

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