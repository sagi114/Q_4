class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def correct_tree(A):
    num=0
    def check_tree(tree_n):
        # -1 means None
        if tree_n is None:
            return -1
        if tree_n.left is not None and tree_n.left.val > tree_n.val :
            tmp=tree_n.val
            tree_n.val=tree_n.left.val
            tree_n.left.val=tmp
            return [tree_n.val, tree_n.left.val]
        if tree_n.right is not None and tree_n.right.val < tree_n.val :
            tmp = tree_n.val
            tree_n.val = tree_n.left.val
            tree_n.left.val = tmp
            return [tree_n.val, tree_n.right.val]
        arr = check_tree(tree_n.right)
        if arr == -1:
            arr = check_tree(tree_n.left)
        return arr

    while check_tree(A) !=-1:
        num+= 1

    return num,A


"""""
if __name__ == '__main__':
    A = TreeNode(1)
    A.left = TreeNode(2)
    A.right = TreeNode(3)
    print(correct_tree(A))
    print(A.val)
    print(f'{A.left.val} A left')
    print(f'{A.right.val} A right')
"""""