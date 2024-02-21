import unittest
from unittest import mock
import builtins
from memory import Memory
from input_output import IO

class TestIOMethods(unittest.TestCase):
    
    def test_read_positive(self):
        memory = Memory()

        with mock.patch.object(builtins, "input", lambda _: "+9000"):
            IO.read(memory, 2)
            self.assertEqual(memory.get_main_memory(2), 9000)

    def test_read_negative(self):
        memory = Memory()

        with mock.patch.object(builtins, "input", lambda _: "-9000"):
            IO.read(memory, 2)
            self.assertEqual(memory.get_main_memory(2), -9000)

    def test_read_syntax_error(self):
        memory = Memory()

        with self.assertRaises(SyntaxError):
            with mock.patch.object(builtins, "input", lambda _: "abcd"):
                IO.read(memory, 2)

    def test_read_overflow_error(self):
        memory = Memory()

        with self.assertRaises(OverflowError):
            with mock.patch.object(builtins, "input", lambda _: "10000"):
                IO.read(memory, 2)

    def test_write_positive(self):
        memory = Memory()
        memory.set_main_memory(2, 9900)

        with mock.patch('builtins.print') as mocked_print:
            IO.write(memory, 2)
            self.assertEqual(mocked_print.mock_calls, [mock.call('9900')])

    def test_write_negative(self):
        memory = Memory()
        memory.set_main_memory(2, -9900)

        with mock.patch('builtins.print') as mocked_print:
            IO.write(memory, 2)
            self.assertEqual(mocked_print.mock_calls, [mock.call('-9900')])

if __name__ == '__main__':
    unittest.main()