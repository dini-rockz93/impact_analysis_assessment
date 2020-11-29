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
            if self.assertEqual(actual, 525) is None:
                print("Success, test case passed")
        except AssertionError:
            print("Test case failed")
     

    def test_case_2(self):
        root = program.BinaryTree(1)
        root.left = program.BinaryTree(2)
        actual = program.nodeDepth(root)
        
        try:
            if self.assertEqual(actual, 3) is None:
                print("Success, test case passed")
        except AssertionError:
            print("Test case failed")
    
    def json_input_tc(self, json_data):
        
        
        root =  program.deserialize(json_data)
        actual = program.nodeDepth(root)
        print(actual)
        try:
            if self.assertEqual(actual, 123) is None:
                print("Success, test case passed")
        except AssertionError:
            print("Test case failed")
        

# sample json format

out = {
    'value': 1, 
    'left': {'value': 2}, 
    'right': {'value': 3, 'left': {'value': 4}, 'right': {'value': 5}}
}


test = TestProgram()
test.test_case_1()
test.test_case_2()
test.json_input_tc(out)

