import pprint, json
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert_bst(root: TreeNode, val:int) -> TreeNode:
    if not root:
        return TreeNode(val)
    if val<root.val:
        root.left = insert_bst(root.left, val)
    else:
        root.right = insert_bst(root.right, val)
    return root

def list_to_bst_tree(data:list) -> TreeNode:
    root = None
    for i in data:
        root = insert_bst(root, i)
    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=' ')
        inorder_traversal(root.right)

def pprint_2(tree_dt):
    print(json.dumps(tree_dt, sort_keys=False, indent=4))
    
def print_tree(node, prefix="", is_left=True):
    """Pretty-print the binary tree sideways."""
    if node:
        print_tree(node.right, prefix + ("│   " if is_left else "    "), False)
        print(prefix + ("└── " if is_left else "┌── ") + str(node.val))
        print_tree(node.left, prefix + ("    " if is_left else "│   "), True)


def traversal_tree_to_dict(root:TreeNode, dt:dict):
    if not dt:
        dt.update({"root":{}})
    # print("dt ==", dt, root.val, root.left, root.right)
    if root.val:
        # print("add root: ", dt)
        dt.update({"root":{"val":root.val}}) 
    if root.left:
        # print("add left: ", dt)
        dt["root"].update({"left":{}})
        traversal_tree_to_dict(root.left, dt["root"]["left"])
    if root.right:
        # print("add right: ", dt)
        dt["root"].update({"right":{}})
        traversal_tree_to_dict(root.right, dt["root"]["right"])


"""
     10 

  4
     5  
"""
# case1 = [10, 4, 5]
# tree_root = list_to_bst_tree(case1)
# tree_dt={}
# # traversal_tree_to_dict(tree_root, tree_dt)
# print(tree_dt)


"""
     2
1        3
"""
case2 = [2,1,3]
tree_root = list_to_bst_tree(case2)
tree_dt={}
traversal_tree_to_dict(tree_root, tree_dt)
# pprint.pprint(tree_dt)
# pprint_2(tree_dt)


"""
               4
         2          7
     1      3    6    9
"""
case3 = [4,2,7,1,3,6,9]
tree_root = list_to_bst_tree(case3)
# print_tree(tree_root)

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        root.left,root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

case2 = [2,1,3]
tree_root = list_to_bst_tree(case2)
print_tree(tree_root)
print("---------after invert----------")
obj_it = Solution().invertTree(tree_root)
print_tree(obj_it)
print("----------------------------------")
case3 = [4,2,7,1,3,6,9]
tree_root = list_to_bst_tree(case3)
print_tree(tree_root)
print("---------after invert----------")
obj_it = Solution().invertTree(tree_root)
print_tree(obj_it)