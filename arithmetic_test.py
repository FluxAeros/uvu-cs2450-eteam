import unittest
from memory import Memory
from arithmetic import Arithmetic

class TestArithmetic(unittest.TestCase):

    def test_add(self):
        memory = Memory()
        memory.set_main_memory(5, 1234)
        memory.set_main_memory(2, 1111)

        Arithmetic.add(memory, 5)
        self.assertEqual(memory.get_accumulator(), 1234)

        Arithmetic.add(memory, 2)
        self.assertEqual(memory.get_accumulator(), 2345)

    def test_subtract(self):
        memory = Memory()
        memory.set_main_memory(5, 1111)
        memory.set_main_memory(2, -3333)

        Arithmetic.subtract(memory, 5)
        self.assertEqual(memory.get_accumulator(), -1111)

        Arithmetic.subtract(memory, 2)
        self.assertEqual(memory.get_accumulator(), 2222)

    def test_multiply(self):
        memory = Memory()
        memory.set_main_memory(5, 100)
        memory.set_main_memory(2, -30)
        Arithmetic.add(memory, 5)

        Arithmetic.multiply(memory, 2)
        self.assertEqual(memory.get_accumulator(), -3000)

    def test_divide(self):
        memory = Memory()
        memory.set_main_memory(5, 3000)
        memory.set_main_memory(2, 33)
        Arithmetic.add(memory, 5)

        Arithmetic.divide(memory, 2)
        self.assertEqual(memory.get_accumulator(), 91)

    def test_arithmeticIndexError(self):
        memory = Memory()

        with self.assertRaises(IndexError):
            Arithmetic.add(memory, 100)
            Arithmetic.subtract(memory, 100)

if __name__ == '__main__':
    unittest.main()

