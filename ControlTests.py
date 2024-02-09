import unittest
from Control import Control
from Memory import Memory
from LoadStore import LoadStore

class TestControlMethods(unittest.TestCase):
    def test_branch(self):
        memory = Memory()
        index = 12

        returnedIndex = Control.Branch(memory, index)
        
        self.assertEqual(index, returnedIndex)

    def test_branchIndexError(self):
        memory = Memory()
        index = 100
        
        with self.assertRaises(IndexError):
            Control.Branch(memory, index)

    def test_branchNeg(self):
        memory = Memory()
        index = 9
        memory.setAccumulator(-1024)

        returnedIndex = Control.BranchNeg(memory, index)

        self.assertEqual(index, returnedIndex)

    def test_branchNegPositiveAccumulator(self):
        memory = Memory()
        index = 11
        memory.setAccumulator(389)

        with self.assertRaises(Exception):
            Control.BranchNeg(memory, index)

    def test_branchNegIndexError(self):
        memory = Memory()
        index = 100
        memory.setAccumulator(-74)

        with self.assertRaises(IndexError):
            Control.BranchNeg(memory, index)

    def test_branchZero(self):
        memory = Memory()
        index = 4
        
        returnedIndex = Control.BranchZero(memory, index)

        self.assertEqual(index, returnedIndex)

    def test_branchZeroNonzeroAccumulator(self):
        memory = Memory()
        index = 15
        memory.setAccumulator(500)

        with self.assertRaises(Exception):
            Control.BranchZero(memory, index)

    def test_branchZeroIndexError(self):
        memory = Memory()
        index = 100
        
        with self.assertRaises(IndexError):
            Control.BranchZero(memory, index)

    def test_halt(self):
        result = Control.Halt()

        self.assertEqual(result, 'halt')
            

if __name__ == '__main__':
    unittest.main()