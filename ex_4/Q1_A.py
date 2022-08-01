class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def check_tree(tree_n):
    # -1 means None
    if tree_n.val is None:
        return -1
    if tree_n.left.val > tree_n.val:
        return [tree_n.val, tree_n.left.val]
    if tree_n.right.val < tree_n.val:
        return [tree_n.val, tree_n.right.val]
    arr = check_tree(tree_n.right)
    if arr == -1:
        arr = check_tree(tree_n.left)
    return arr
"""""
if __name__ == '__main__':
    A = TreeNode(1)
    A.left = TreeNode(2)
    A.right = TreeNode(3)
    print(check_tree(A))
"""""


