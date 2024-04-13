import unittest
from control import Control
from memory import Memory
from load_store import LoadStore

class TestControlMethods(unittest.TestCase):
    def test_branch(self):
        memory = Memory()
        index = 12

        returned_index = Control.branch(memory, index)
        
        self.assertEqual(index, returned_index)

    def test_branch_index_error(self):
        memory = Memory()
        index = 251
        
        with self.assertRaises(IndexError):
            Control.branch(memory, index)

    def test_branch_neg(self):
        memory = Memory()
        index = 9
        memory.set_accumulator(-1024)

        returned_index = Control.branch_neg(memory, index)

        self.assertEqual(index, returned_index)

    def test_branch_neg_positive_accumulator(self):
        memory = Memory()
        index = 11
        memory.set_accumulator(389)

        self.assertEqual(Control.branch_neg(memory, index), 'no_branch')
            

    def test_branch_neg_index_error(self):
        memory = Memory()
        index = 251
        memory.set_accumulator(-74)

        with self.assertRaises(IndexError):
            Control.branch_neg(memory, index)

    def test_branch_zero(self):
        memory = Memory()
        index = 4
        
        returned_index = Control.branch_zero(memory, index)

        self.assertEqual(index, returned_index)

    def test_branch_zero_nonzero_accumulator(self):
        memory = Memory()
        index = 15
        memory.set_accumulator(500)

        self.assertEqual(Control.branch_zero(memory, index), 'no_branch')

    def test_branch_zero_index_error(self):
        memory = Memory()
        index = 251
        
        with self.assertRaises(IndexError):
            Control.branch_zero(memory, index)

    def test_halt(self):
        result = Control.halt()

        self.assertEqual(result, 'halt')
            

if __name__ == '__main__':
    unittest.main()
