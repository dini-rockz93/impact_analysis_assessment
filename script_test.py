import script_app as program

import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = program.BinaryTree(1)
        root.left = program.BinaryTree(2)
        root.left.left = program.BinaryTree(4)
        root.left.left.left = program.BinaryTree(8)
        root.left.left.right = program.BinaryTree(9)
        root.left.right = program.BinaryTree(5)
        root.right = program.BinaryTree(3)
        root.right.left = program.BinaryTree(6)
        root.right.right = program.BinaryTree(7)
        print(root)
        actual = program.nodeDepth(root)
        try:
            if self.assertEqual(actual, 26) is None:
                print("Success, test case passed")
        except AssertionError:
            print("Test case failed")
     

    def test_case_2(self):
        root = program.BinaryTree(1)
        root.left = program.BinaryTree(2)
        actual = program.nodeDepth(root)
        try:
            if self.assertEqual(actual, 1) is None:
                print("Success, test case passed")
        except AssertionError:
            print("Test case failed")

test = TestProgram()
test.test_case_1()
test.test_case_2()

