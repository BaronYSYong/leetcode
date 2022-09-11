"""
Given two binary trees and imagine that when you put one of them to 
cover the other, some nodes of the two trees are overlapped while the 
others are not.

You need to merge them into a new binary tree. The merge rule is that 
if two nodes overlap, then sum node values up as the new value of the 
merged node. Otherwise, the NOT null node will be used as the node of 
new tree.

Example 1:
Input: 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
Output: 
Merged tree:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7
Note: The merging process must start from the root nodes of both trees.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mergeTrees1(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        time: 108 ms (recursive)
        """
        if t1 is None:
            if t2 is None:
                return None
            return t2
        if t2 is None:
            return t1
        t1.val += t2.val
        t1.left = self.mergeTrees1(t1.left, t2.left)
        t1.right = self.mergeTrees1(t1.right, t2.right)
        return t1

    def mergeTrees2(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        time: 146 ms
        """
        if not t1 and not t2: return None
        merge = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))
        merge.left = self.mergeTrees2(t1 and t1.left, t2 and t2.left)
        merge.right = self.mergeTrees2(t1 and t1.right, t2 and t2.right)
        return merge
    
    def tree2Dict(self, tree, layer, dictItem):
        if tree:
            try:
                dictItem[layer].append(tree.val)
            except KeyError:
                dictItem.update({layer:[tree.val]})
            layer += 1
            self.tree2Dict(tree.left,layer,dictItem)  
            self.tree2Dict(tree.right,layer,dictItem)
        else:
            try:
                dictItem[layer].append(None)
            except KeyError:
                dictItem.update({layer:[None]})        

if __name__ == '__main__':
    tree = Solution()
    
    t1 = TreeNode(1)
    t1.left = TreeNode(3)
    t1.right = TreeNode(2)    
    t1.left.left = TreeNode(5)
    dict1 = {}
    tree.tree2Dict(t1,0,dict1)
    
    t2 = TreeNode(2)
    t2.left = TreeNode(1)
    t2.right = TreeNode(3)
    t2.left.right = TreeNode(4)
    t2.right.right = TreeNode(7)
    dict2 = {}
    tree.tree2Dict(t2,0,dict2)
    
    tree = Solution()
    tree.mergeTrees1(t1,t2)

    dict3 = {}
    tree.tree2Dict(t1,0,dict3)
    print dict1
    print dict2
    print dict3
