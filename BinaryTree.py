class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    def insert_left(self, new_data):
        if self.left == None:
            self.left = BinaryTree(new_data)
        else:
            t = BinaryTree(new_data, left=self.left)
            self.left = t
    def insert_right(self, new_data):
        if self.right == None:
            self.right = BinaryTree(new_data)
        else:
            t = BinaryTree(new_data, right=self.right)
            self.right = t
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

def create_bst_from_sorted_list(sorted_list):
    if not sorted_list:
        return None

    middle_index = len(sorted_list) // 2
    middle_value = sorted_list[middle_index]

    left_sublist = sorted_list[:middle_index]
    right_sublist = sorted_list[middle_index + 1:]

    tree = BinaryTree(middle_value, left=create_bst_from_sorted_list(left_sublist), right=create_bst_from_sorted_list(right_sublist))

    return tree

def print_tree(t, level):
    print(' ' * (level*4) + str(t.get_data())) 
    if t.get_left() != None:
        print('(L)', end = '')
        print_tree(t.get_left(), level + 1) 
    if t.get_right() != None: 
        print('(R)', end = '')
        print_tree(t.get_right(), level + 1)


tree = create_bst_from_sorted_list([1,2,3,4,5,6])
print_tree(tree, 0)

