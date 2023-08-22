edges = [[0,1,4],[2,3,1]]

def mst(edges,n):
    '''
        given teh edges of a graph, kruskal's algorithm
        finds the minimum spanning tree using the union find (also called disjoint set)
        data stucture. at every iteration, we choose the smallest possible edge weight.
        if the chosen edge forms a cycle (end points within same component) we choose to ignore
        the edge. we do so until we choose n-1 edges (where n is the number of nodes in the graph)
    '''

    par = [i for i in range(n)] # initalize parent as the node itself
    rank = [1 for i in range(n)] # initialize rank as 1

    def find(node):
        p = par[node]
        while p!=par[p]:
            par[p] = par[par[p]]
            p = par[p]
        return p
    
    def union(a,b):
        pa,pb = find(a),find(b)
        if pa==pb:
            return False
        if rank[pa]>rank[pb]:
            rank[pa] += rank[pb]
            par[pb] = pa
        else:
            rank[pb] += rank[pa]
            par[pa] = pb
        return True

    # sort all the edges based on the weights
    edges.sort(key=lambda x: x[2])

    # choose edges
    count = n-1
    spanning_tree = []
    for edge in edges:
        [a,b,weight] = edge
        if not union(a,b):
            # this edge forms a cycle so ignore it
            continue
        spanning_tree.append(edge)
        count -= 1
        if count == 0:
            break
    
    return spanning_tree
