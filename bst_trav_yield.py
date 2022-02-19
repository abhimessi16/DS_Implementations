"""
traversing a tree using inorder, but using "yield" statement.
learning to use "yield from" to store recursive return values.
working fine, but turns out it's not as memory efficient as expected,
maybe need to work on a better implementation.

Used in a leetcode problem, and was pretty slow and memory inefficient.
"""
class Node:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

def inorder(root):
    if root:
        yield from inorder(root.left)
        yield root.val
        yield from inorder(root.right)

n1=Node(3)
n2=Node(2)
n3=Node(1)
n4=Node(5)
n5=Node(4)
n1.left=n2
n2.left=n3
n1.right=n4
n4.left=n5

ans=inorder(n1)
f1,f2=0,0
n1=ans.__next__()
while 1:
    try:
        print(n1)
        n1=ans.__next__()
    except:
        break
print(n1)
print(ans.__next__())