import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        dic={}
        def f(root,val):
            if root==None:
                return
            dic[root.data]=val
            f(root.left,val+1)
            f (root.right,val+1)
        f(root,0)
        k=sorted(dic.items(),key=lambda x:x[1])
        s=""
        for i in k:
            s+=str(i[0])
            s+=" "
        print(s)


T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
