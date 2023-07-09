import unittest


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST(object):
    def __init__(self):
        self.root = None

    # Pega o número de elementos usando recursão. Complexidade O(logN)

    def get_root(self):
        return self.root

    def size(self):
        return self.recur_size(self.root)

    def recur_size(self, root):
        if root is None:
            return 0
        else:
            return 1 + self.recur_size(root.left) + self.recur_size(root.right)

    # Busca dados no BST usando recursão. Complexidade O(logN)

    def search(self, data):
        return self.recur_search(self.root, data)

    def recur_search(self, root, data):
        if root is None:
            return False
        if root.data == data:
            return True
        elif data > root.data:
            return self.recur_search(root.right, data)
        else:
            return self.recur_search(root.left, data)

    # Inserindo dado no BST usando recursão. Complexidade O(logN)

    def insert(self, data):
        if self.root:
            return self.recur_insert(self.root, data)
        else:
            self.root = Node(data)
            return True

    def recur_insert(self, root, data):
        if root.data == data:
            return False
        elif data < root.data:
            if root.left:
                return self.recur_insert(root.left, data)
            else:
                root.left = Node(data)
                return True
        else:
            if root.right:
                return self.recur_insert(root.right, data)
            else:
                root.right = Node(data)
                return True

    # Pré-ordem, pós-ordem, travessia de ordem BST

    def preorder(self, root):
        if root:
            print(str(root.data), end=' ')
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(str(root.data), end=' ')
            self.inorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(str(root.data), end=' ')


class TestSuite(unittest.TestCase):
    def setUp(self):
        self.tree = BST()
        self.tree.insert(10)
        self.tree.insert(15)
        self.tree.insert(6)
        self.tree.insert(4)
        self.tree.insert(9)
        self.tree.insert(12)
        self.tree.insert(24)
        self.tree.insert(7)
        self.tree.insert(20)
        self.tree.insert(30)
        self.tree.insert(18)

    def test_search(self):
        self.assertTrue(self.tree.search(24))
        self.assertFalse(self.tree.search(50))

    def test_size(self):
        self.assertEqual(11, self.tree.size())


if __name__ == '__main__':
    unittest.main()





















