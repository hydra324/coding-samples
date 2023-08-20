arr = [1,2,3,4,0,5]
par = [i for i in range(len(arr))]
rank = [1]* len(arr)

def find(node):
    node = par[node]
    while node!=par[node]:
        # path compression
        par[node] = par[par[node]]
        node = par[node]
    return node

def union(a,b):
    par_a,par_b = find(a),find(b)
    if par_a==par_b:
        return # no need to join
    # find the smaller group and merge it into larger group
    if rank[par_a] < rank[par_b]:
        rank[par_b] += rank[par_a]
        par[par_a] = par_b
    else:
        rank[par_a] += rank[par_b]
        par[par_b] = par_a
    return