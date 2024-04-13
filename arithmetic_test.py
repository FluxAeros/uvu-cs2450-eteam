import unittest
from memory import Memory
from arithmetic import Arithmetic

class TestArithmetic(unittest.TestCase):

    def test_add(self):
        memory = Memory()
        memory.set_accumulator(0)
        memory.set_main_memory(5, 1234)
        memory.set_main_memory(2, 1111)
        memory.set_main_memory(11, 9999)

        Arithmetic.add(memory, 5)
        self.assertEqual(memory.get_accumulator(), 1234)

        Arithmetic.add(memory, 2)
        self.assertEqual(memory.get_accumulator(), 2345)

        Arithmetic.add(memory, 11)
        self.assertEqual(memory.get_accumulator(), 12344)

    def test_subtract(self):
        memory = Memory()
        memory.set_accumulator(0)
        memory.set_main_memory(5, 1111)
        memory.set_main_memory(2, 3333)

        Arithmetic.subtract(memory, 5)
        self.assertEqual(memory.get_accumulator(), -1111)

        Arithmetic.subtract(memory, 2)
        self.assertEqual(memory.get_accumulator(), -4444)  # As per 6 digit overflow

    def test_multiply(self):
        memory = Memory()
        memory.set_accumulator(0)
        memory.set_main_memory(5, 100)
        memory.set_main_memory(2, -30)
        memory.set_accumulator(100)  # Correcting the setup

        Arithmetic.multiply(memory, 2)
        self.assertEqual(memory.get_accumulator(), -3000)

    def test_divide(self):
        memory = Memory()
        memory.set_accumulator(0)
        memory.set_main_memory(5, 3000)
        memory.set_main_memory(2, 33)
        memory.set_accumulator(3000)  # Correcting the setup

        Arithmetic.divide(memory, 2)
        self.assertEqual(memory.get_accumulator(), 91)

    def test_overflow(self):
        memory = Memory()
        memory.set_accumulator(0)
        memory.set_main_memory(5, 999999)
        memory.set_main_memory(2, 999999)
        Arithmetic.add(memory, 5)

        Arithmetic.multiply(memory, 2)
        # After multiplication and handling of overflow:
        self.assertEqual(memory.get_accumulator(), 999998000001 % 1000000)  # Proper 6-digit overflow

    def test_index_error(self):
        memory = Memory()
        with self.assertRaises(IndexError):
            Arithmetic.add(memory, 251)  # Testing with a non-existent memory index
            Arithmetic.subtract(memory, 251)

if __name__ == '__main__':
    unittest.main()
