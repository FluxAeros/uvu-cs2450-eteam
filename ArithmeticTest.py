import unittest
from Memory import Memory
from Arithmetic import Arithmetic

class testArithmetic(unittest.TestCase):

    def test_add(self):
        memory = Memory()
        memory.setMainMemory(5, 1234)
        memory.setMainMemory(2, 1111)
        memory.setMainMemory(11, 9999)

        Arithmetic.Add(memory, 5)
        self.assertEqual(memory.getAccumulator(), 1234)

        Arithmetic.Add(memory, 2)
        self.assertEqual(memory.getAccumulator(), 2345)

        Arithmetic.Add(memory, 11)
        self.assertEqual(memory.getAccumulator(), 2344)

    def test_subtract(self):
        memory = Memory()
        memory.setMainMemory(5, 1111)
        memory.setMainMemory(2, -3333)

        Arithmetic.Subtract(memory, 5)
        self.assertEqual(memory.getAccumulator(), -1111)

        Arithmetic.Subtract(memory, 2)
        self.assertEqual(memory.getAccumulator(), 2222)

    def test_multiply(self):
        memory = Memory()
        memory.setMainMemory(5, 100)
        memory.setMainMemory(2, -30)
        Arithmetic.Add(memory, 5)

        Arithmetic.Multiply(memory, 2)
        self.assertEqual(memory.getAccumulator(), -3000)

    def test_divide(self):
        memory = Memory()
        memory.setMainMemory(5, 3000)
        memory.setMainMemory(2, 33)
        Arithmetic.Add(memory, 5)

        Arithmetic.Divide(memory, 2)
        self.assertEqual(memory.getAccumulator(), 91)

    def test_arithmeticIndexError(self):
        memory = Memory()

        with self.assertRaises(IndexError):
            Arithmetic.Add(memory, 100)
            Arithmetic.Subtract(memory, 100)

    def test_overflow(self):
        memory = Memory()
        memory.setMainMemory(5, 9999)
        memory.setMainMemory(2, 9999)
        Arithmetic.Add(memory, 5)

        Arithmetic.Multiply(memory, 2)
        self.assertEqual(memory.getAccumulator(), 1)

if __name__ == '__main__':
    unittest.main()
