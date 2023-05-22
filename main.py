class BinarySearchTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert(self, new_data):
        if new_data == self.data:
            return
        elif new_data < self.data:
            if self.left == None:
                self.left = BinarySearchTree(new_data)
            else:
                self.left.insert(new_data)
        else:
            if self.right == None:
                self.right = BinarySearchTree(new_data)
            else:
                self.right.insert(new_data)

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    def contains(self, value):
        if self.data == value:
            return True
        elif value < self.data and self.left != None:
            return self.left.contains(value)
        elif value > self.data and self.right != None:
            return self.right.contains(value)
        else:
            return False
        
def print_tree(t, level):
    print(' ' * (level*4) + str(t.get_data())) 
    if t.get_left() != None:
        print('(L)', end = '')
        print_tree(t.get_left(), level + 1) 
    if t.get_right() != None: 
        print('(R)', end = '')
        print_tree(t.get_right(), level + 1)

def create_bst_from_list(values):
    tree = BinarySearchTree(values[0])
    for index in range(1, len(values)):
        tree.insert(values[index])
    return tree

def get_difference_beneath(tree, value):
    if tree is None:
        return 0

    if tree.data == value:
        left_sum = sum_tree_values(tree.left) if tree.left else 0
        right_sum = sum_tree_values(tree.right) if tree.right else 0
        return left_sum - right_sum

    if value < tree.data:
        return get_difference_beneath(tree.left, value)
    else:
        return get_difference_beneath(tree.right, value)

def sum_tree_values(node):
    if node is None:
        return 0

    return node.data + sum_tree_values(node.left) + sum_tree_values(node.right)



tree = create_bst_from_list([27,14,35,10,19,31,42])
# print_tree(tree, 0)

print('Sum beneath 5 =', get_difference_beneath(tree, 5))
print('Sum beneath 14 =', get_difference_beneath(tree, 14))







