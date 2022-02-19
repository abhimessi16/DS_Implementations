"""
finding all the possible paths using dfs,
similar to using bactracking
"""

def dfs(graph,src,dest,path):
    if src==dest:
        paths.append(path[:])
    else:
        for x in graph[src]:
            if x not in path:
                path.append(x)
                dfs(graph,x,dest,path)
                path.pop()

def allPaths(graph,src,dest):
    path=[]
    path=[src]
    dfs(graph,src,dest,path)

def depthFirstSearch(graph,src,vis=set()):
    for v in graph[src]:
        if v not in vis:
            print(v)
            vis.add(v)
            depthFirstSearch(graph,v,vis)
    

paths=[]
g={0:[1,3,2],1:[0,4,5],2:[0,4],3:[0,4],4:[2,3,1,5],5:[1,4]}
depthFirstSearch(g,5)