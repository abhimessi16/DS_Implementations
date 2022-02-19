"""
working on mst using kruskal, without using disjoint set to detect cycle
using dfs to detect cycle
the algorithm still needs some work
"""

from collections import defaultdict as dd

def detectCycle(graph,src):
    key=list(graph.keys())
    if not key:
        return False
    s=[key[0]]
    vis=set()
    while s:
        ele=s.pop(0)
        vis.add(ele)
        for x,w in graph[ele]:
            if x not in vis:
                if src in s:
                    return True
                s.append(x)
    return False

def sortHelp(graph,edgesCount):
    edges=[]
    vis=set()
    for edge in graph:
        u=edge
        for v,w in graph[edge]:
            if (v,u) not in vis:
                edges.append((w,(u,v)))
                vis.add((u,v))
    return sorted(edges)

def kruskal(graph,edgesCount):
    mst=dd(set)
    c=0
    edges=sortHelp(graph,edgesCount)
    for edge in edges:
        if c==(edgesCount-1):
            return mst
        u,v,w=edge[1][0],edge[1][1],edge[0]
        print(u,v,w)
        if not detectCycle(mst,u):
            mst[u].add((v,w))
            c+=1
        if not detectCycle(mst,v):
            mst[v].add((v,w))
            c+=1
    return

g={'a':[('b',3),('c',5)],'b':[('d',4),('e',2)],'c':[],'d':[('e',6)],'e':[]}
print(kruskal(g,5))