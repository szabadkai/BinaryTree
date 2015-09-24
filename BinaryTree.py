class BinaryTree:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None
        self.list = {key: True}

    def __iter__(self):
        for node in self.tree_data():
            yield node
            
    def __getitem__(self, item):
        found = self
        while found.key != item:
            if found.key == item:
                return found.data
            elif self.key < item:
                if found.right is None:
                    return None
                found = found.right
            else:
                if found.left is None:
                    return None
                found = found.left
        return found.data

    def insert(self, key, data):
        if self.key < key:
            if self.right is None:
                self.right = BinaryTree(key, data)
            else:
                self.right.insert(key, data)
        elif self.key > key:
            if self.left is None:
                self.left = BinaryTree(key, data)
            else:
                self.left.insert(key, data)
        else:
            self.key = key
            self.data = data

    @property
    def min(self):
        min = self
        while min.left is not None:
            min = min.left
        return min.key

    @property
    def max(self):
        max = self
        while max.right is not None:
            max = max.right
        return max.key

    def children_count(self):
        count = 0
        if self.left:
            count += 1
        if self.right:
            count += 1
        return count

    def descendant_count(self):
        count = 0
        if self.left:
            count += 1 + self.left.descendant_count()
        if self.right:
            count += 1 + self.right.descendant_count()
        return count

    def tree_data(self):
        """
        Generator to get the tree nodes data
        """
        # we use a stack to traverse the tree in a non-recursive way
        stack = []
        node = self
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:  # we are returning so we pop the node and we yield it
                node = stack.pop()
                yield node
                node = node.right
