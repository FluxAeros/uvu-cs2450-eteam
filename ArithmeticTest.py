import unittest
from Memory import Memory
from Arithmetic import Arithmetic

class testArithmetic(unittest.TestCase):

    def test_add(self):
        memory = Memory()
        memory.mainMemory[5] = 1234
        memory.mainMemory[2] = 1111

        Arithmetic.Add(memory, 5)
        self.assertEqual(memory.accumulator, 1234)

        Arithmetic.Add(memory, 2)
        self.assertEqual(memory.accumulator, 2345)

    def test_subtract(self):
        memory = Memory()
        memory.mainMemory[5] = 1111
        memory.mainMemory[2] = -3333

        Arithmetic.Subtract(memory, 5)
        self.assertEqual(memory.accumulator, -1111)

        Arithmetic.Subtract(memory, 2)
        self.assertEqual(memory.accumulator, 2222)

    def test_multiply(self):
        memory = Memory()
        memory.mainMemory[5] = 100
        memory.mainMemory[2] = -30
        Arithmetic.Add(memory, 5)

        Arithmetic.Multiply(memory, 2)
        self.assertEqual(memory.accumulator, -3000)

    def test_divide(self):
        memory = Memory()
        memory.mainMemory[5] = 3000
        memory.mainMemory[2] = 33
        Arithmetic.Add(memory, 5)

        Arithmetic.Divide(memory, 2)
        self.assertEqual(memory.accumulator, 91)

    def test_arithmeticIndexError(self):
        memory = Memory()

        with self.assertRaises(IndexError):
            Arithmetic.Add(memory, 100)
            Arithmetic.Subtract(memory, 100)

if __name__ == '__main__':
    unittest.main()
