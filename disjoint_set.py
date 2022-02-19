"""
using disjoint set is interesting and fun.
have to work on on the fly implementations

satisfactory.
"""

class DisjointSet:
   
    def __init__(self,vertices):
        self.vertices={}
        self.rank={}
        for vertice in vertices:
            self.vertices[vertice]=vertice
            self.rank[vertice]=1
       
    def find(self, vertice):
        verts=[]
        while vertice!=self.vertices[vertice]:
            vertice=self.vertices[vertice]
            verts.append(vertice)
        for x in verts:
            self.vertices[x]=vertice
        return vertice
   
    def union(self, vertice1, vertice2):
        root1=self.find(vertice1)
        root2=self.find(vertice2)
        if root1!=root2:
            self.vertices[root2]=root1
            self.rank[root1]+=1
   
    def union_rank(self, vertice1, vertice2):
        root1=self.find(vertice1)
        root2=self.find(vertice2)
        if root1!=root2:
            if self.rank[root1]>self.rank[root2]:
                self.vertices[root2]=root1
            elif self.rank[root2]>self.rank[root1]:
                self.vertices[root1]=root2
            else:
                self.vertices[root2]=root1
                self.rank[root1]+=1
       
    def connected(self, vertice1, vertice2):
        return self.find(vertice1)==self.find(vertice2)
   
verts=list("dcab")
dset=DisjointSet(verts)
dset.union_rank(verts[0],verts[3])
dset.union_rank(verts[1],verts[2])
dset.union_rank(verts[0],verts[2])
print(dset.vertices)
print(dset.rank)
for x in verts:
    print(dset.find(x))