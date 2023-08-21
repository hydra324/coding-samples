# DFS version of topo sort algorithm taken from
# wikipedia at https://en.wikipedia.org/wiki/Topological_sorting

def toposort(graph,nodes):
    ordered_list = [] # list to store the topological order
    perm_marker,temp_marker = set(), set() # initialize visited sets for temporary and permananet markers
    def dfs(node):
        if node in perm_marker:
            # already visited node
            return False
        if node in temp_marker:
            # we got a cycle bruh
            return True
        temp_marker.add(node)
        for nei in graph[node]:
            if dfs(nei):
                return True
        temp_marker.remove(node)
        perm_marker.add(node)
        ordered_list = [node] + ordered_list # add node to the head of the list
    
    for node in nodes:
        if node not in perm_marker:
            if dfs(node):
                return "Cycle found"
    return ordered_list