import unittest
from unittest import mock
import builtins
from Memory import Memory
from IO import IO

class TestIOMethods(unittest.TestCase):
    
    def test_readPositive(self):
        mem = Memory()

        with mock.patch.object(builtins, "input", lambda _: "+9000"):
            IO.Read(mem, 2)
            self.assertEqual(mem.getMainMemory(2), 9000)

    def test_readNegative(self):
        mem = Memory()

        with mock.patch.object(builtins, "input", lambda _: "-9000"):
            IO.Read(mem, 2)
            self.assertEqual(mem.getMainMemory(2), -9000)

    def test_readSyntaxError(self):
        mem = Memory()

        with self.assertRaises(SyntaxError):
            with mock.patch.object(builtins, "input", lambda _: "abcd"):
                IO.Read(mem, 2)

    def test_readOverflowError(self):
        mem = Memory()

        with self.assertRaises(OverflowError):
            with mock.patch.object(builtins, "input", lambda _: "10000"):
                IO.Read(mem, 2)

    def test_writePositive(self):
        mem = Memory()
        mem.setMainMemory(2, 9900)

        with mock.patch('builtins.print') as mocked_print:
            IO.Write(mem, 2)
            self.assertEqual(mocked_print.mock_calls, [mock.call('9900')])

    def test_writeNegative(self):
        mem = Memory()
        mem.setMainMemory(2, -9900)

        with mock.patch('builtins.print') as mocked_print:
            IO.Write(mem, 2)
            self.assertEqual(mocked_print.mock_calls, [mock.call('-9900')])

if __name__ == '__main__':
    unittest.main()