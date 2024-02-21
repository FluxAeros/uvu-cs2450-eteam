import unittest
from load_store import LoadStore
from memory import Memory

class TestLoadStoreMethods(unittest.TestCase):

    def test_load(self):
        memory = Memory()
        memory.set_main_memory(3, 1024)

        LoadStore.load(memory, 3)

        self.assertEqual(memory.get_accumulator(), 1024)
    
    def test_load_index_error(self):
        memory = Memory()

        with self.assertRaises(IndexError):
            LoadStore.load(memory, 100)

    def test_store(self):
        memory = Memory()
        memory.set_accumulator(1024)

        LoadStore.store(memory, 3)

        self.assertEqual(memory.get_main_memory(3), 1024)
    
    def test_store_index_error(self):
        memory = Memory()

        with self.assertRaises(IndexError):
            LoadStore.store(memory, 100)

if __name__ == '__main__':
    unittest.main()