import unittest
from Memory import Memory
from Arithmetic import Arithmetic

class testArithmetic(unittest.TestCase):

    def test_add(self):
        memory = Memory()
        memory.mainMemory[5] = 1234
        memory.mainMemory[2] = 1111

        Arithmetic.add(memory, 5)
        self.assertEqual(memory.accumulator, 1234)

        Arithmetic.add(memory, 2)
        self.assertEqual(memory.accumulator, 2345)

    def test_subtract(self):
        memory = Memory()
        memory.mainMemory[5] = 1111
        memory.mainMemory[2] = -3333

        Arithmetic.subtract(memory, 5)
        self.assertEqual(memory.accumulator, -1111)

        Arithmetic.subtract(memory, 2)
        self.assertEqual(memory.accumulator, 2222)

    def test_arithmeticIndexError(self):
        memory = Memory()

        with self.assertRaises(IndexError):
            Arithmetic.add(memory, 100)
            Arithmetic.subtract(memory, 100)

if __name__ == '__main__':
    unittest.main()
